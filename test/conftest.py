import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


with open("../config.yaml", "r") as f:
    config = yaml.safe_load(f)


@pytest.fixture(scope="session")
def config_data():
    return config


@pytest.fixture(scope="function")
def driver(config_data):
    options = webdriver.ChromeOptions()
    if config_data["browser"]["headless"]:
        options.add_argument("--headless=new")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    driver.maximize_window()
    driver.implicitly_wait(config_data["timeouts"]["implicit_wait"])
    yield driver
    driver.quit()