# notify.py
import asyncio
import httpx

USER_ID = "500357318613925889"
WEBHOOK_URL = "https://discord.com/api/webhooks/1359216089023906063/9PLtNmPUoSwm8UUStyxZzpxVjALWFdKcULtRF3kBJVBzBsVywnXZ4OmvInk8Tt5IhQdW"

# client riutilizzato (evita handshake TCP ad ogni notifica)
_client: httpx.AsyncClient | None = None


async def _get_client() -> httpx.AsyncClient:
    global _client
    if _client is None:
        _client = httpx.AsyncClient(timeout=10)
    return _client


async def send_notification(content: str):
    payload = {
        "content": f"{content}! <@{USER_ID}>",
        "allowed_mentions": {"users": [USER_ID]},
    }

    try:
        client = await _get_client()
        r = await client.post(WEBHOOK_URL, json=payload)

        # Discord webhook: 204 = OK
        if r.status_code == 204:
            print("Notifica inviata")
        else:
            print(f"Webhook status: {r.status_code} | {r.text}")

    except httpx.RequestError as e:
        print(f"Errore notifica: {e}")
