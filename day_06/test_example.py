import os
import dotenv


def setup_module():
    dotenv.load_dotenv("./.env")


def test_get_env_account():
    print(os.getenv("ACCOUNT"))


def test_get_env_password():
    print(os.getenv("PASSWORD"))
