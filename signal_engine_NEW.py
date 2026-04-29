# signal_engine.py

from itertools import combinations
from signal_threshold import THRESHOLDS


def _extract_prices(kyber_snapshot):
    """
    Estrae prezzi normalizzati dalle simulazioni valide.
    """
    valid = [s for s in kyber_snapshot if s.get("ok") is True]

    prices = []

    for s in valid:
        try:
            amount_in = float(s["amount_in"])
            amount_out = float(s["amount_out"])

            if amount_in == 0:
                continue

            price = amount_out / amount_in

            prices.append({
                "chain": s["chain"],
                "price": price
            })
        except Exception:
            continue

    return prices


def _compute_pairwise_diffs(prices):
    """
    Calcola tutte le differenze percentuali pairwise.

    Output:
    [
        {"chain": "base-bsc", "diff": "1.23"},
        ...
    ]
    """
    diffs = []

    for a, b in combinations(prices, 2):
        if a["price"] >= b["price"]:
            high, low = a, b
        else:
            high, low = b, a

        # differenza percentuale rispetto al low (importante!)
        diff_pct = ((high["price"] - low["price"]) / low["price"]) * 100

        diffs.append({
            "chain": f"{high['chain']}-{low['chain']}",
            "diff": f"{diff_pct:.2f}"
        })

    return diffs


def _compute_signals(diffs, active_token):
    """
    Confronta ogni diff con le soglie e genera segnali validi.
    """
    signals = []

    token_rules = THRESHOLDS[active_token]

    for d in diffs:
        pair = d["chain"]
        diff_val = float(d["diff"])

        # soglia specifica o default
        rule = token_rules.get(pair, token_rules["default"])
        min_spread = rule["min_spread"]

        if diff_val >= min_spread:
            sell_chain, buy_chain = pair.split("-")

            signal = {
                "sell_chain": sell_chain,
                "buy_chain": buy_chain,
                "spread": diff_val,
                "diffs": {
                    sell_chain: diff_val,
                    buy_chain: 0.0,  # baseline implicita
                },
                "threshold_used": rule,
                "_edge": diff_val - min_spread,  # per ranking interno
            }

            print("🚨 SIGNAL:", signal)
            signals.append(signal)

    return signals


def _select_best_signal(signals):
    """
    Seleziona il segnale con massimo scostamento dalla soglia.
    """
    if not signals:
        return None

    best = max(signals, key=lambda s: s["_edge"])

    # rimuove campo interno
    best.pop("_edge", None)

    return best


def evaluate(kyber_snapshot, active_token):
    """
    Entry point unico.

    Flow:
    - estrae prezzi
    - calcola differenze pairwise
    - genera segnali
    - seleziona il migliore

    Ritorna:
        best_signal oppure None
    """

    prices = _extract_prices(kyber_snapshot)

    if len(prices) < 2:
        return None

    diffs = _compute_pairwise_diffs(prices)

    signals = _compute_signals(diffs, active_token)

    best_signal = _select_best_signal(signals)

    return best_signal
