import asyncio
import subprocess

from worker_automate_hub.tasks.task_definitions import task_definitions
from worker_automate_hub.utils.logger import setup_logger

logger = setup_logger("executor_logger", "app.log")


async def run_process(process_name, task):
    try:
        result = subprocess.run(
            ["python", process_name, task["uuidProcesso"], task["nomProcesso"]],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        logger.error(f"Erro ao executar o process {process_name}: {e}")
        return None


async def perform_task(task):
    try:
        print(f"Processo a ser executado: {task['nomProcesso']}")
        logger.info(f"Processo a ser executado: {task['nomProcesso']}")
        task_uuid = task["uuidProcesso"]
        if task_uuid in task_definitions:
            process_name = task_definitions[task_uuid]
            result = await run_process(process_name, task)
            return result
        else:
            logger.error(f"Processo não encontrado: {task_uuid}")
            return None
    except Exception as e:
        logger.error(f"Erro ao performar o processo: {e}")
