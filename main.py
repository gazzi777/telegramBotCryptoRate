import os
# Launch our server via pywebio
import pywebio
import threading
from pywebio.output import *
import pywebio.input as inp

from handlers.parser import check_coins_balance
from handlers.menu import TaskHandler


# Creating a dark theme on the site
@pywebio.config(theme="dark")
async def main():
    clear()
    threading.Thread(target=check_coins_balance).start()

    task = TaskHandler()
    logo_path = os.path.join("data", "logo.jpg")
    put_image(open(logo_path, "rb").read())

    # Creating an interface
    method = await inp.select(
        "Выберите нужный вариант",
        [
            "Добавить задание",
            "Список заданий"
        ])

    if "Добавить задание" == method:
        await task.add_task_in_list()
    elif "Список заданий" == method:
        task.get_task_list()


if __name__ == "__main__":
    # Write our host and port
    pywebio.start_server(main, host="0.0.0.0", port=4444)
