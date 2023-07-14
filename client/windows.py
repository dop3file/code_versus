import time
import asyncio
from typing import Iterable
from collections import defaultdict
from getpass import getpass
from abc import abstractmethod

from utils import clear_screen, back_handler
from jwt import JWTAuth, AuthData
from exceptions import catch_exception, Unauthorized
from dependencies import *


class BaseWindow:
    def __init__(self, jwt: JWTAuth):
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
    def __init__(self, jwt: JWTAuth):
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
    def __init__(self, jwt: JWTAuth):
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

    @back_handler
    def check_tasks(self):
        ...

    @back_handler
    def get_profile(self):
        ...

    def quit(self):
        self.jwt.quit()
        clear_screen()

    def exit(self):
        print("Bye!")
        exit(0)

