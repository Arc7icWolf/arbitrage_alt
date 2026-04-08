import aiohttp
from decimal import Decimal, ROUND_DOWN
import asyncio

from kyber_chains import TOKENS
from monitoring import simulate_swap
from kyber_payload import build_swap_payload
from profit_check import is_swap_profitable

import sys


def get_chain_cfg(
    active_token: str, chain_name: str, *, override_amount_in=None
) -> dict:
    """
    Restituisce la configurazione della chain corretta per il token attivo.
    """
    try:
        cfg = TOKENS[active_token][chain_name].copy()  # ✅ nuova struttura
    except KeyError:
        raise ValueError(f"Chain {chain_name} non trovata per token {active_token}")

    if override_amount_in is not None:
        cfg["amount_in"] = str(override_amount_in)

    return cfg


async def confirm_signal(active_token: str, signal: dict, amount_in: float) -> dict:
    """
    1) BUY token -> SPS (o DEC)
    2) SELL SPS (o DEC) -> token
    """
    buy_chain = signal["buy_chain"]
    sell_chain = signal["sell_chain"]

    async with aiohttp.ClientSession() as session:

        # === 1️⃣ BUY: token_in -> SPS ===
        buy_cfg = get_chain_cfg(active_token, buy_chain, override_amount_in=amount_in)

        # ✅ simulate_swap ora richiede chain_name + cfg
        buy_result = await simulate_swap(session, buy_chain, buy_cfg)

        if not buy_result.get("ok"):
            return {"ok": False, "stage": "buy", "error": buy_result}

        # === PAYLOAD BUY ===
        MAX_RETRY = 3
        for attempt in range(1, MAX_RETRY + 1):
            payload_result = await build_swap_payload(
                session,
                buy_chain,
                route_summary=buy_result["route"]["routeSummary"],
            )

            if payload_result["ok"]:
                break

            if attempt < MAX_RETRY:
                await asyncio.sleep(0.5)
            else:
                return {
                    "ok": False,
                    "stage": "payload",
                    "reason": payload_result,
                }

        # === COMMISSIONI: denormalizzazione (human -> raw) ===
        amount_human = buy_result["amount_out"]

        # ✅ lookup corretta dei decimali per la chain di destinazione
        decimals = TOKENS[active_token][sell_chain]["token_out_decimals"]

        raw_out = int(
            (Decimal(str(amount_human)) * (Decimal(10) ** decimals)).to_integral_value(
                rounding=ROUND_DOWN
            )
        )

        # === 2️⃣ SELL: SPS -> token_in ===
        sell_cfg = get_chain_cfg(
            active_token,
            sell_chain,
            override_amount_in=raw_out,  # usa il valore denormalizzato
        )

        # inverti token_in / token_out per lo swap inverso
        sell_cfg["token_in"], sell_cfg["token_out"] = (
            sell_cfg["token_out"],
            sell_cfg["token_in"],
        )

        sell_result = await simulate_swap(session, sell_chain, sell_cfg)
        if not sell_result.get("ok"):
            return {"ok": False, "stage": "sell", "error": sell_result}

        # === 3️⃣ PROFIT CHECK ===
        amount_in_eth = buy_cfg["amount_in"]
        amount_out_eth = sell_result["amount_out"]

        decimals = TOKENS[active_token][sell_chain]["token_in_decimals"]

        raw_amount_out_eth = int(
            (
                Decimal(str(amount_out_eth)) * (Decimal(10) ** decimals)
            ).to_integral_value(rounding=ROUND_DOWN)
        )

        buy_gas_price = Decimal(buy_result.get("gas_price", 0))
        sell_gas_price = Decimal(sell_result.get("gas_price", 0))

        if buy_chain == "bsc":
            buy_gas_price /= 15
        if sell_chain == "bsc":
            sell_gas_price /= 15

        gas_cost_eth = str(
            Decimal(buy_result.get("gas", 0)) * buy_gas_price
            + Decimal(sell_result.get("gas", 0)) * sell_gas_price
        )

        if not is_swap_profitable(
            amount_in=amount_in_eth,
            amount_out=raw_amount_out_eth,
            gas_cost_eth=gas_cost_eth,
        ):
            return {
                "ok": False,
                "stage": "profit_check",
                "reason": "not_profitable",
                "signal": signal,
                "buy": buy_result,
                "buy_payload": payload_result["tx"],
                "sell": sell_result,
                "final_amount_out": sell_result["amount_out"],
            }

    return {
        "ok": True,
        "signal": signal,
        "buy": buy_result,
        "buy_payload": payload_result["tx"],
        "sell": sell_result,
        "final_amount_out": sell_result["amount_out"],
        "token_in": buy_cfg["token_in"],
        "amount_in": buy_result["amount_in"],
    }
