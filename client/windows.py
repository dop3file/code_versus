import time
import asyncio
from typing import Iterable
from collections import defaultdict
from getpass import getpass
from abc import abstractmethod
import os

from utils import clear_screen, back_handler, get_text_from_file
from jwt import JWTApi, Task
from exceptions import catch_exception, Unauthorized
from dependencies import *


class BaseWindow:
    def __init__(self, jwt: JWTApi):
        self.jwt = jwt
        self.output_window()

    @abstractmethod
    def output_window(self):
        ...

    def typo(self):
        console.print("[info]Некоректный ввод[/info]")
        time.sleep(1)
        clear_screen()
        self.output_window()

    def back(self):
        clear_screen()
        self.output_window()

    def execute_command(self):
        command = input(">> ")
        self.commands[command]()


class AuthWindow(BaseWindow):
    def __init__(self, jwt: JWTApi):
        self.commands = defaultdict(lambda: self.typo)
        self.commands.update({
            "1": self.login,
            "2": self.register
        })
        if not asyncio.run(jwt.prefetch_auth()):
            super().__init__(jwt)

    def output_window(self):
        console.print("Привет!", style="yellow")
        console.print("Это консольный клиент [italic red]Code versus[/italic red] - платформы для решения алгоритмических задачек")
        console.print("\n1. Войти\n2. Зарегистрироваться")
        self.execute_command()

    @back_handler
    def login(self):
        try:
            data = {}
            data["username"] = input("Введите логин: ")
            data["password"] = getpass(prompt="Введите пароль: ")
            asyncio.run(self.jwt.login(data))
            console.print("Вы успешло вошли!", style="green")
        except Unauthorized as e:
            console.print(e.message)
            self.output_window()

    @back_handler
    @catch_exception
    def register(self):
        data = {}
        data["email"] = input("Введите email: ")
        data["username"] = input("Введите username: ")
        data["password"] = getpass("Введите пароль: ")
        password2 = getpass("Введите пароль(повторно): ")
        data["first_name"] = input("Введите ваше имя: ")
        data["last_name"] = input("Введите вашу фамилию: ")
        if data["password"] != password2:
            console.print("Пароли не совпадают!", style="bold red")
            return self.registration()
        response = asyncio.run(self.jwt.register(data))
        if response.is_ok:
            console.print("[green]Регистрация прошла успешно![/green]")
        else:
            for key, value in response.data.items():
                if isinstance(value, Iterable):
                    for item in value:
                        console.print(item, style="bold red")
                else:
                    console.print(value)


class MainWindow(BaseWindow):
    def __init__(self, jwt: JWTApi):
        self.commands = defaultdict(lambda: self.typo)
        self.commands.update({
            "1": self.check_tasks,
            "2": self.get_profile,
            "3": self.exit,
            "4": self.quit
        })
        super().__init__(jwt)

    def output_window(self):
        console.print(f"[info]Привет, {self.jwt.user.username}!")
        console.print("1 - просмотреть задачки")
        console.print("2 - мой профиль")

        console.print("3 - [warning]выйти[/warning]")
        console.print("4 - [error]выйти с аккаунта[/error]")
        self.execute_command()

    def check_tasks(self):
        task_window = TaskWindow(self.jwt)

    @back_handler
    def get_profile(self):
        user = asyncio.run(self.jwt.get_user()).data
        console.print(f"Никнейм - {user['username']}\nEmail - {user['email']}\nРейтинг - {user['rating']}\nКол-во выполненных задач - {user['count_submit_task']}")
        blank_input = input("Ctrl+C чтобы выйти")

    def quit(self):
        self.jwt.quit()
        clear_screen()

    def exit(self):
        print("Bye!")
        exit(0)


class TaskWindow(BaseWindow):
    def __init__(self, jwt: JWTApi):
        self.jwt = jwt
        self.tasks = asyncio.run(self.jwt.get_tasks())
        super().__init__(jwt)

    @back_handler
    def output_window(self):
        clear_screen()
        for idx, task in enumerate(self.tasks):
            console.print(f"{idx + 1} - [{task.level.lower()}]{task.title}[/{task.level.lower()}]")

        try:
            menu_option = int(input("Введите номер задачи: "))
            if 0 <= menu_option - 1 <= len(self.tasks) - 1:
                self.run_task(self.tasks[menu_option - 1])
            else:
                self.back()
        except ValueError:
            self.back()

    @back_handler
    def run_task(self, task: Task):
        clear_screen()
        console.print(f"[info]Название[/info] - {task.title}")
        console.print(f"[info]Уровень[/info] - [{task.level.lower()}]{task.title}[/{task.level.lower()}]")
        console.print(f"[info]Описание[/info] - {task.description}")
        task_path = input("Введите полный путь до решения задачи: ")
        if os.path.exists(task_path):
            console.print("[info]Решение отправлено на тестирование![/info]")
            test_group = asyncio.run(self.jwt.solve_task(task.id, get_text_from_file(task_path)))
            console.print(f"Статус решения - [{'success' if test_group['status'] else 'error'}]{'OK' if test_group['status'] else 'WRONG'}[/{'success' if test_group['status'] else 'error'}]")
        else:
            console.print("Неверный путь!", style="bold red")

    def back(self):
        clear_screen()
        MainWindow(self.jwt)
