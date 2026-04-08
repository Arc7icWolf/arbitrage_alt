import asyncio
import time

from kyber_chains import TOKENS
from monitoring import take_kyber_snapshot
from kyber_diff_from_mean import compute_diff_from_mean
from signal_engine import evaluate
from notify import send_notification
from signal_confirmation import confirm_signal

"""
from a_sign_send import send_swap
from a_notify import notify
"""


async def main():
    """
    Entry point principale dell'arbitrage engine.
    Qui vengono orchestrate le varie fasi del flow.
    """

    for active_token in TOKENS:
        start = time.time()

        kyber_snapshot = await take_kyber_snapshot(active_token)

        diffs = compute_diff_from_mean(kyber_snapshot)

        for k in kyber_snapshot:
            print(
                f"chain: {k['chain']}, ok: {k['ok']}, "
                f"amount in: {k.get('amount_in', [])}, amount out: {k.get('amount_out', [])}, "
                f"gas: {k.get('gas', [])}, gas price: {k.get('gas_price', [])}"
            )

        for d in diffs:
            print(d)

        signal = evaluate(diffs, active_token)

        if signal:
            print("✅ BEST SIGANL:", signal)
            await send_notification(f"✅ BEST SIGANL: {signal}")

            # c'è da sistemare profit_check, perchè le gas fees
            # sono calcolate in ETH: forse conviene controllare a quanto
            # ammontano e procedere solo se costano meno di 2 centesimi di dollaro;
            # inoltre c'è da aggiungere le commissioni di across: anche qui forse basta
            # togliere un paio di centesimi dal risultato
            result = await confirm_signal(active_token, signal, amount_in=None)

            if not result["ok"]:
                print(f"Tentativo di swap interrotto: {result['stage']}")
                continue

            print(f"🧪 Tentativo di swap avviato: {result}")

            await notify(f"🧪 Tentativo di swap in corso: {result['signal']}")

            continue

            # -----------------------------
            # Firma e invio
            # -----------------------------
            dry_run = True  # Imposta su False per effettuare transazioni

            tx_hash = await send_swap(result, dry_run=dry_run)

            if tx_hash:
                end = time.time()
                print(f"Tempo impiegato: {end - start} secondi")
                if dry_run:
                    print("🟢 Dry run OK — la tx non revertirebbe")
                else:
                    print(f"🚀 Transaction inviata: 0x{tx_hash}")
                break

        time.sleep(5)

    return


if __name__ == "__main__":
    asyncio.run(main())
