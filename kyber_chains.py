# kyber_chains.py

AMOUNT_IN = int(10000 * 10**18)  # ETH

TOKENS = {
    "SPS": [
        {
            "name": "ethereum",
            "token_in": "0x00813E3421E1367353BfE7615c7f7f133C89df74",
            "token_out": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", # USDC
            "token_out_decimals": 6,
            "amount_in": str(10000 * 10**18), # 10.000 SPS
        },
        {
            "name": "bsc",
            "token_in": "0x1633b7157e7638C4d6593436111Bf125Ee74703F",
            "token_out": "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d", # USDC
            "token_out_decimals": 18,
            "amount_in": str(10000 * 10**18), # 10.000 SPS
        },
        {
            "name": "base",
            "token_in": "0x578661e9a09eee6b2cd97d4ded1ccbae7b8516b9",
            "token_out": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913", # USDC
            "token_out_decimals": 6,
            "amount_in": str(10000 * 10**18), # 10.000 SPS
        },
    ],

    "DEC": [
        {
            "name": "ethereum",
            "token_in": "0x9393fdc77090F31c7db989390D43F454B1A6E7F3",
            "token_out": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", # USDC
            "token_out_decimals": 6,
            "amount_in": str(1 * 10**8), # 100.000 DEC
        },
        {
            "name": "bsc",
            "token_in": "0xE9D7023f2132D55cbd4Ee1f78273CB7a3e74F10A",
            "token_out": "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d", # USDC
            "token_out_decimals": 18,
            "amount_in": str(1 * 10**8), # 100.000 DEC
        },
    ],
}
