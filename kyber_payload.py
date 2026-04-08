# a_kyber_payload.py
import aiohttp

from my_address import USER_ADDRESS

BASE_URL = "https://aggregator-api.kyberswap.com"
HEADERS = {"accept": "application/json"}


async def build_swap_payload(session, chain_name: str, route_summary: dict) -> dict:
    url = f"{BASE_URL}/{chain_name}/api/v1/route/build"

    payload = {
        "routeSummary": route_summary,
        "slippage": 1,
        "userAddress": USER_ADDRESS,
        "recipient": USER_ADDRESS,
    }

    async with session.post(url, json=payload, headers=HEADERS, timeout=10) as r:
        data = await r.json()

        if r.status != 200 or "data" not in data:
            return {"ok": False, "error": data}

        return {"ok": True, "tx": data["data"]}
