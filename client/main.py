from jwt import JWTApi
from windows import AuthWindow, MainWindow


jwt = JWTApi()


if __name__ == "__main__":
    try:
        while True:
            auth_window = AuthWindow(jwt)
            main_window = MainWindow(jwt)
    except KeyboardInterrupt:
        print("Пока!")



