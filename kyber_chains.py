# kyber_chains.py

AMOUNT_IN = int(0.01 * 10**18)  # ETH

TOKENS = {
    "SPS": [
        {
            "name": "ethereum",
            "token_in": "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",  # ETH
            "token_out": "0x00813E3421E1367353BfE7615c7f7f133C89df74",
            "amount_in": str(AMOUNT_IN),
        },
        {
            "name": "bsc",
            "token_in": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
            "token_out": "0x1633b7157e7638C4d6593436111Bf125Ee74703F",
            "amount_in": str(AMOUNT_IN),
        },
        {
            "name": "base",
            "token_in": "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",
            "token_out": "0x578661e9a09eee6b2cd97d4ded1ccbae7b8516b9",
            "amount_in": str(AMOUNT_IN),
        },
    ],

    "DEC": [
        {
            "name": "ethereum",
            "token_in": "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",
            "token_out": "0x9393fdc77090F31c7db989390D43F454B1A6E7F3",
            "amount_in": str(AMOUNT_IN),
        },
        {
            "name": "bsc",
            "token_in": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
            "token_out": "0xE9D7023f2132D55cbd4Ee1f78273CB7a3e74F10A",
            "amount_in": str(AMOUNT_IN),
        },
    ],
}
