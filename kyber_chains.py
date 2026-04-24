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
            "amount_in": str(20 * 10**6),  # 20.000 DEC
        },
        "bsc": {
            "token_in": "0xE9D7023f2132D55cbd4Ee1f78273CB7a3e74F10A",
            "token_out": "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d",  # USDC
            "token_in_decimals": 6,
            "token_out_decimals": 18,
            "amount_in": str(20 * 10**6),  # 20.000 DEC
        },
    },
    "COMP": {
        "bsc": {
            "token_in": "0x52ce071bd9b1c4b00a0b92d298c512478cad67e8",
            "token_out": "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d",  # USDC
            "token_in_decimals": 18,
            "token_out_decimals": 18,
            "amount_in": str(5 * 10**17),  # 0.5 COMP
        },
        "base": {
            "token_in": "0x9e1028F5F1D5eDE59748FFceE5532509976840E0",
            "token_out": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",  # USDC
            "token_in_decimals": 18,
            "token_out_decimals": 6,
            "amount_in": str(5 * 10**17),  # 0.5 COMP
        },
        "arbitrum": {
            "token_in": "0x354A6dA3fcde098F8389cad84b0182725c6C91dE",
            "token_out": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
            "token_in_decimals": 18,
            "token_out_decimals": 6, 
            "amount_in": str(5 * 10**17),  # 0.5 COMP
        },
    },
    "SAND": {
        "bsc": {
            "token_in": "0x67b725d7e342d7B611fa85e859Df9697D9378B2e",
            "token_out": "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d",  # USDC
            "token_in_decimals": 18,
            "token_out_decimals": 18,
            "amount_in": str(150 * 10**18),  # 150 SAND
        },
        "base": {
            "token_in": "0xac531Eb26Ca1d21b85126De8FB87E80E09002DcF",
            "token_out": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",  # USDC
            "token_in_decimals": 18,
            "token_out_decimals": 6,
            "amount_in": str(150 * 10**18),  # 150 SAND
        },
        "polygon": {
            "token_in": "0xBbba073C31bF03b8ACf7c28EF0738DeCF3695683",
            "token_out": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",  # USDC (Polygon)
            "token_in_decimals": 18,
            "token_out_decimals": 6,
            "amount_in": str(150 * 10**18),  # 150 SAND
        },
    },
}


'''
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
            "token_out": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
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
'''
