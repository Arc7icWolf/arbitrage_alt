def compute_diff_from_mean(kyber_snapshot):
    """
    Calcola la differenza percentuale di ogni simulazione
    rispetto alla media dei risultati.
    """

    # Estraiamo solo snapshot validi
    valid = [s for s in kyber_snapshot if s.get("ok") is True]

    if not valid:
        return []

    # Calcolo del "prezzo" normalizzato per chain
    prices = []

    for s in valid:
        amount_in = float(s["amount_in"])
        amount_out = float(s["amount_out"])

        price = amount_out / amount_in

        prices.append({"chain": s["chain"], "price": price})

    # Media dei prezzi
    mean_price = sum(p["price"] for p in prices) / len(prices)

    # Calcolo deviazione percentuale dalla media
    diffs = []

    for p in prices:
        diff_pct = ((p["price"] - mean_price) / mean_price) * 100

        diffs.append({"chain": p["chain"], "diff": f"{diff_pct:.2f}"})

    return diffs