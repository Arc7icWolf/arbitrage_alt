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
            "min_spread": 1.2,
        },
        "base-bsc": {
            "min_spread": 1.2,
        },
        # ===== DEFAULT =====
        "default": {
            "min_spread": 1.2,
        },
    },
    "DEC": {
        # ===== SPECIFICHE =====
        "ethereum-bsc": {
            "min_spread": 3,
        },
        "bsc-ethereum": {
            "min_spread": 3.5,
        },
        # ===== DEFAULT =====
        "default": {
            "min_spread": 2,
        },
    },
    "COMP": {
        # ===== SPECIFICHE =====
        "bsc-arbitrum": {
            "min_spread": 1,
        },
        "arbitrum-bsc": {
            "min_spread": 1,
        },
        "bsc-base": {
            "min_spread": 1,
        },
        "base-bsc": {
            "min_spread": 1,
        },
        "arbitrum-base": {
            "min_spread": 1,
        },
        "base-arbitrum": {
            "min_spread": 1,
        },
        # ===== DEFAULT =====
        "default": {
            "min_spread": 1,
        },
    },
    "SAND": {
        # ===== SPECIFICHE =====
        "bsc-polygon": {
            "min_spread": 1,
        },
        "polygon-bsc": {
            "min_spread": 1,
        },
        "bsc-base": {
            "min_spread": 1,
        },
        "base-bsc": {
            "min_spread": 1,
        },
        "polygon-base": {
            "min_spread": 1,
        },
        "base-polygon": {
            "min_spread": 1,
        },
        # ===== DEFAULT =====
        "default": {
            "min_spread": 1,
        },
    },
}



'''
"TRUF": {
        # ===== SPECIFICHE =====
        "ethereum-arbitrum": {
            "min_spread": 0.5,
        },
        "arbitrum-ethereum": {
            "min_spread": 0.5,
        },
        "ethereum-base": {
            "min_spread": 0.5,
        },
        "base-ethereum": {
            "min_spread": 0.5,
        },
        "arbitrum-base": {
            "min_spread": 0.5,
        },
        "base-arbitrum": {
            "min_spread": 0.5,
        },
        # ===== DEFAULT =====
        "default": {
            "min_spread": 0.5,
        },
    },
'''
