import aiohttp
import asyncio
from kyber_chains import TOKENS

BASE_URL = "https://aggregator-api.kyberswap.com"
HEADERS = {"x-client-id": "snapshot-script"}


import asyncio


async def simulate_swap(session, chain_cfg, retries: int = 5):
    """
    Simula uno swap tokenIn -> tokenOut su una singola chain.
    Ritenta fino a `retries` volte se la risposta non è valida.
    """

    url = f"{BASE_URL}/{chain_cfg['name']}/api/v1/routes"

    params = {
        "tokenIn": chain_cfg["token_in"],
        "tokenOut": chain_cfg["token_out"],
        "amountIn": chain_cfg["amount_in"],
    }

    last_error = None

    for attempt in range(1, retries + 1):
        print(f"Attempt n. {attempt} for {chain_cfg["name"]}")
        try:
            async with session.get(
                url, params=params, headers=HEADERS, timeout=10
            ) as r:
                try:
                    data = await r.json(content_type=None)
                except Exception:
                    data = None

                # --- risposta buona ---
                if r.status == 200 and "data" in data:
                    route = data["data"]
                    summary = route.get("routeSummary")

                    # ---- VALIDAZIONE REALE DELLA QUOTE ----
                    valid = (
                        summary
                        and isinstance(summary.get("amountOut"), (str, int))
                        and int(summary["amountOut"]) > 0
                    )

                    if valid:
                        return {
                            "chain": chain_cfg["name"],
                            "ok": True,
                            "amount_in": summary["amountIn"],
                            "amount_out": summary["amountOut"],
                            "gas": summary.get("gas"),
                            "gas_price": summary.get("gasPrice"),
                            "route": route,
                        }

                    # falliti tutti i tentativi
                    return last_error or {
                        "chain": chain_cfg["name"],
                        "ok": False,
                        "reason": "unknown_failure",
                    }

        except Exception as e:
            # --- errore di rete / timeout ---
            last_error = {
                "chain": chain_cfg["name"],
                "ok": False,
                "exception": str(e),
                "attempt": attempt,
            }

        # backoff progressivo (molto corto, adatto arbitraggio)
        if attempt < retries:
            await asyncio.sleep(0.15 * attempt)

    # falliti tutti i tentativi
    return last_error


async def take_kyber_snapshot(active_token):
    """
    Restituisce una lista di simulazioni swap, una per chain.
    """
    async with aiohttp.ClientSession() as session:
        while True:
            tasks = [simulate_swap(session, chain_cfg) for chain_cfg in TOKENS[active_token]]
            return await asyncio.gather(*tasks)


if __name__ == "__main__":
    snapshots = asyncio.run(take_kyber_snapshot())

    for s in snapshots:
        print(s)
