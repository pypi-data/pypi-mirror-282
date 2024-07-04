import psutil
from prompt_toolkit.shortcuts import checkboxlist_dialog, radiolist_dialog
from rich.console import Console

from worker_automate_hub.config.settings import (
    load_env_config,
    load_worker_config,
)

console = Console()


async def get_system_info():
    worker_config = load_worker_config()
    max_cpu = psutil.cpu_percent(interval=10.0)
    cpu_percent = psutil.cpu_percent(interval=1.0)
    memory_info = psutil.virtual_memory()

    return {
        "uuidRobo": worker_config["UUID_ROBO"],
        "maxCpu": f"{max_cpu}",
        "maxMem": f"{memory_info.total / (1024 ** 3):.2f}",
        "usoCpu": f"{cpu_percent}",
        "usoMem": f"{memory_info.used / (1024 ** 3):.2f}",
        "situacao": "{'status': 'em desenvolvimento'}",
    }


async def get_new_task_info():
    env_config = load_env_config()
    worker_config = load_worker_config()
    return {
        "uuidRobo": worker_config["UUID_ROBO"],
        "versao": env_config["VERSION"],
    }


def multiselect_prompt(options, title="Select options"):
    result = checkboxlist_dialog(
        values=[(option, option) for option in options],
        title=title,
        text="Use space to select multiple options.\nPress Enter to confirm your selection.",
    ).run()

    if result is None:
        console.print("[red]No options selected.[/red]")
    else:
        return result


def select_prompt(options, chave_1, title="Selecione uma opção"):
    values = [(index, option[chave_1]) for index, option in enumerate(options)]

    result = radiolist_dialog(
        values=values,
        title=title,
        text="Use as teclas de seta para navegar e Enter para selecionar uma opção.",
    ).run()

    if result is None:
        console.print("[red]Nenhuma opção selecionada.[/red]")
    else:
        # Retorna o dicionário correspondente ao índice selecionado
        return options[result]
