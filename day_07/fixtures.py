import pytest
from dotenv import load_dotenv


@pytest.fixture(scope="function", name="init", autouse=False)
def load_env():
    load_dotenv("./.env")
