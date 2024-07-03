import os

import aiohttp
import requests
from rich.console import Console

from worker_automate_hub.api.helpers.api_helpers import handle_api_response
from worker_automate_hub.utils.logger import setup_logger
from worker_automate_hub.utils.util import get_new_task_info, get_system_info

logger = setup_logger("client_logger", "app.log")
console = Console()


async def get_new_task():
    try:
        from worker_automate_hub.config.settings import (
            API_AUTHORIZATION,
            API_BASE_URL,
        )

        headers_basic = {"Authorization": f"Basic {API_AUTHORIZATION}"}
        data = await get_new_task_info()

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{API_BASE_URL}/robo/new-job",
                data=data,
                headers=headers_basic,
            ) as response:
                return await handle_api_response(response)

    except Exception as e:
        logger.error(f"Erro ao obter nova tarefa: {e}")
        console.print(
            f"Erro ao obter nova tarefa: {e}",
            style="bold red",
        )
        return None


async def notify_is_alive():
    try:
        from worker_automate_hub.config.settings import (
            API_AUTHORIZATION,
            API_BASE_URL,
        )

        headers_basic = {"Authorization": f"Basic {API_AUTHORIZATION}"}
        data = await get_system_info()

        async with aiohttp.ClientSession() as session:
            async with session.put(
                f"{API_BASE_URL}/robo/last-alive",
                data=data,
                headers=headers_basic,
            ) as response:
                return await handle_api_response(response, last_alive=True)

    except Exception as e:
        logger.error(f"Erro ao informar is alive: {e}")
        console.print(
            f"Erro ao informar is alive: {e}",
            style="bold red",
        )
        return None


async def get_workers():
    try:
        from worker_automate_hub.config.settings import (
            API_AUTHORIZATION,
            API_BASE_URL,
        )

        headers_basic = {"Authorization": f"Basic {API_AUTHORIZATION}"}

        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{API_BASE_URL}/robo/workers",
                headers=headers_basic,
            ) as response:
                return await response.json()

    except Exception as e:
        logger.error(f"Erro ao obter a lista de workers: {e}")
        console.print(
            f"Erro ao obter a lista de workers: {e}",
            style="bold red",
        )
        return None


def read_secret(path):
    from worker_automate_hub.config.settings import VAULT_TOKEN, VAULT_URL

    url = f"{VAULT_URL}/v1/secret/{path}"
    headers = {"X-Vault-Token": VAULT_TOKEN}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


def load_environments(env: str):
    from worker_automate_hub.config.settings import get_package_version

    environments = {}
    if env == "teste":
        environments["local"] = (
            {
                "API_BASE_URL": "http://127.0.0.1:3002/automate-hub",
                "VERSION": get_package_version("worker-automate-hub"),
                "NOTIFY_ALIVE_INTERVAL": "30",
                "API_AUTHORIZATION": os.getenv("API_AUTHORIZATION", ""),
                "LOG_LEVEL": "30",
            },
        )
        return environments["local"]
    else:
        environments[env] = read_secret(f"{env}-sim/api-automate-hub")

        return environments[env]
