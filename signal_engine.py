# signal_engine.py

from itertools import combinations

from signal_threshold import THRESHOLDS


def normalize_entries(diffs):
    """
    Normalizza l'input in una struttura uniforme.
    """
    return [
        {
            "chain": d["chain"],
            "diff": float(d["diff"]),
        }
        for d in diffs
    ]


def compute_signals(entries, active_token):
    """
    Genera tutti i segnali validi basati sulle soglie.
    """
    signals = []

    for a, b in combinations(entries, 2):
        # determina direzione
        if a["diff"] >= b["diff"]:
            high, low = a, b
        else:
            high, low = b, a

        spread = high["diff"] - low["diff"]
        key = f"{high['chain']}-{low['chain']}"

        # soglia specifica o default
        rule = THRESHOLDS[active_token].get(key, THRESHOLDS[active_token]["default"])
        min_spread = rule["min_spread"]

        if spread >= min_spread:
            signal = {
                "buy_chain": high["chain"],
                "sell_chain": low["chain"],
                "spread": spread,
                "diffs": {
                    high["chain"]: high["diff"],
                    low["chain"]: low["diff"],
                },
                "threshold_used": key if key in THRESHOLDS else "default",
            }

            print("🚨 SIGNAL:", signal)
            signals.append(signal)

    return signals


def select_best_signal(signals):
    """
    Seleziona il segnale con spread massimo.
    """
    if not signals:
        return None

    return max(signals, key=lambda s: s["spread"])


def evaluate(diffs, active_token):
    """
    Entry point principale.

    - normalizza input
    - calcola segnali
    - seleziona il migliore
    """

    entries = normalize_entries(diffs)

    signals = compute_signals(entries, active_token)
    best_signal = select_best_signal(signals)

    if not best_signal:
        return None

    return best_signal
