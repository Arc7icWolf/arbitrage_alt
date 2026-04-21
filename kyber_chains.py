# kyber_chains.py

AMOUNT_IN = int(10000 * 10**18)  # ETH

TOKENS = {
    "SPS": {
        "ethereum": {
            "token_in": "0x00813E3421E1367353BfE7615c7f7f133C89df74",
            "token_out": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",  # USDC
            "token_in_decimals": 18,
            "token_out_decimals": 6,
            "amount_in": str(10000 * 10**18),  # 10.000 SPS
        },
        "bsc": {
            "token_in": "0x1633b7157e7638C4d6593436111Bf125Ee74703F",
            "token_out": "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d",  # USDC
            "token_in_decimals": 18,
            "token_out_decimals": 18,
            "amount_in": str(10000 * 10**18),  # 10.000 SPS
        },
        "base": {
            "token_in": "0x578661e9a09eee6b2cd97d4ded1ccbae7b8516b9",
            "token_out": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",  # USDC
            "token_in_decimals": 18,
            "token_out_decimals": 6,
            "amount_in": str(10000 * 10**18),  # 10.000 SPS
        },
    },
    "DEC": {
        "ethereum": {
            "token_in": "0x9393fdc77090F31c7db989390D43F454B1A6E7F3",
            "token_out": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",  # USDC
            "token_in_decimals": 6,
            "token_out_decimals": 6,
            "amount_in": str(2 * 10**7),  # 20.000 DEC
        },
        "bsc": {
            "token_in": "0xE9D7023f2132D55cbd4Ee1f78273CB7a3e74F10A",
            "token_out": "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d",  # USDC
            "token_in_decimals": 6,
            "token_out_decimals": 18,
            "amount_in": str(2 * 10**7),  # 20.000 DEC
        },
    },
    "TRUF": {
        "ethereum": {
            "token_in": "0x243c9be13fAbA09F945ccc565547293337Da0Ad7",
            "token_out": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",  # USDC
            "token_in_decimals": 18,
            "token_out_decimals": 6,
            "amount_in": str(2500 * 10**18),  # 2.500 TRUF
        },
        "arbitrum": {
            "token_in": "0xB59c8912c83157a955f9D715E556257F432C35D7",
            "token_out": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831"
            "token_in_decimals": 18,
            "token_out_decimals": 6, 
            "amount_in": str(2500 * 10**18),  # 2.500 TRUF
        },
        "base": {
            "token_in": "0xB59c8912c83157a955f9D715E556257F432C35D7",
            "token_out": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",  # USDC
            "token_in_decimals": 18,
            "token_out_decimals": 6,
            "amount_in": str(2500 * 10**18),  # 2.500 TRUF
        },
    },   
}
