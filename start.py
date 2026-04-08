import asyncio
import time

from kyber_chains import TOKENS
from monitoring import take_kyber_snapshot
from kyber_diff_from_mean import compute_diff_from_mean
from signal_engine import evaluate
from notify import send_notification

'''
from a_kyber_simulation import simulate_signal
from a_sign_send import send_swap
from a_notify import notify
'''

import sys


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
        
        signal = evaluate(diffs)
        
        if signal:
            print("✅ BEST SIGANL:", signal)
            await send_notification(f"✅ BEST SIGANL: {signal}")

            sys.exit()
            # amount_in = 
            
            result = await simulate_signal(signal, amount_in)

            if not result["ok"]:
                print(f"Tentativo di swap interrotto: {result['stage']}")
                continue

            print(f"🧪 Tentativo di swap avviato: {result}")

            await notify(
                f"🧪 Tentativo di swap in corso per 0.0{str(amount_in)[:3]} ETH: {result['signal']}"
            )

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
