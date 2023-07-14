from jwt import JWTAuth
from windows import AuthWindow, MainWindow


jwt = JWTAuth()


if __name__ == "__main__":
    try:
        while True:
            auth_window = AuthWindow(jwt)
            main_window = MainWindow(jwt)
    except KeyboardInterrupt:
        print("Пока!")



