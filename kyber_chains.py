# kyber_chains.py

AMOUNT_IN = int(0.01 * 10**18)  # ETH

CHAINS = [
    {
        "name": "ethereum",
        "token_in": "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",  # ETH
        "token_out": "0x00813E3421E1367353BfE7615c7f7f133C89df74",  # SPS
        "amount_in": str(AMOUNT_IN),
    },
    {
        "name": "bsc",
        "token_in": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",  # WETH (BSC)
        "token_out": "0x1633b7157e7638C4d6593436111Bf125Ee74703F",  # SPS (BSC)
        "amount_in": str(AMOUNT_IN),
    },
    {
        "name": "base",
        "token_in": "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",  # ETH (Base)
        "token_out": "0x578661e9a09eee6b2cd97d4ded1ccbae7b8516b9",  # SPS (Base)
        "amount_in": str(AMOUNT_IN),
    },
]
