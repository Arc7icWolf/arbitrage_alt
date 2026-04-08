# signal_threshold.py

THRESHOLDS = {
    "SPS": {
        # ===== SPECIFICHE =====
        "ethereum-bsc": {
            "min_spread": 3,
        },
        "bsc-ethereum": {
            "min_spread": 3.5,
        },
        "ethereum-base": {
            "min_spread": 3,
        },
        "base-ethereum": {
            "min_spread": 3.5,
        },
        "bsc-base": {
            "min_spread": 1.5,
        },
        "base-bsc": {
            "min_spread": 1.5,
        },
        # ===== DEFAULT =====
        "default": {
            "min_spread": 1.5,
        },
    },
    "DEC": {
        # ===== SPECIFICHE =====
        "ethereum-bsc": {
            "min_spread": 2,
        },
        "bsc-ethereum": {
            "min_spread": 3,
        },
        # ===== DEFAULT =====
        "default": {
            "min_spread": 2,
        },
    },
}
