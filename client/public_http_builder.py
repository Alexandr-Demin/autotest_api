from httpx import Client
from client.event_hooks import curl_event_hook
from config import setting


def get_public_http_client() -> Client:
    """
    Функция создаёт экземпляр httpx.Client с базовыми настройками.

    :return: Готовый к использованию объект httpx.Client.
    """
    return Client(
        timeout=setting.http_client.timeout,
        base_url=setting.http_client.client_url,
        event_hooks={"request": [curl_event_hook]}
        )