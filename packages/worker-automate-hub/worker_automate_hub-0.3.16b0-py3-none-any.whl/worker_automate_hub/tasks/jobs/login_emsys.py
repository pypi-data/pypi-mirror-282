import asyncio
import subprocess

import pyautogui
import win32gui  # type: ignore


# Função para localizar a janela do EmSys
def find_emsys_window(title):
    def enum_window_callback(hwnd, windows):
        if title in win32gui.GetWindowText(hwnd):
            windows.append(hwnd)

    windows = []
    win32gui.EnumWindows(enum_window_callback, windows)
    return windows[0] if windows else None


async def start_emsys(executable_path):
    subprocess.Popen(executable_path)
    print("EmSys iniciado.")


async def wait_for_window(title):
    hwnd = None
    while hwnd is None:
        hwnd = await asyncio.get_event_loop().run_in_executor(
            None, find_emsys_window, title
        )
        await asyncio.sleep(1)
    return hwnd


async def wait_for_interface_ready(delay):
    await asyncio.sleep(delay)


async def fill_credentials(username, password):
    pyautogui.write(username)
    pyautogui.press("tab")
    pyautogui.write(password)
    pyautogui.press("enter")


async def main(username, password, executable_path, window_title):
    try:
        await start_emsys(executable_path)
        hwnd = await wait_for_window(window_title)
        print("Janela do EmSys encontrada.")
        await wait_for_interface_ready(5)
        await fill_credentials(username, password)
        print("Login realizado com sucesso.")
    except Exception as e:
        print(f"Erro ao realizar login no EmSys: {e}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 5:
        print(
            "Uso: python login_emsys.py <username> <password> <executable_path> <window_title>"
        )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    executable_path = "C:\Rezende\EMSys3\EMSys3.exe"  # sys.argv[3]
    window_title = "EMSys3"  # sys.argv[4]

    asyncio.run(main(username, password, executable_path, window_title))
