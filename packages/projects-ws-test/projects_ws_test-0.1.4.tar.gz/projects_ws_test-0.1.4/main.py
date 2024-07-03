import sys
from app.login_as_user import login_as_user


def main():
    try:
        login_as_user()
    except ValueError as ve:
        return str(ve)




if __name__ == "__main__":
    main()