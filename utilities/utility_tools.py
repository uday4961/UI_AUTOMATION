# utilities/utility_tools.py
import logging
import os
from datetime import datetime

# GET PROJECT ROOT PATH (this is the magic line!)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# CREATE FOLDERS IN ROOT (not inside utilities!)
os.makedirs(os.path.join(PROJECT_ROOT, "logs"), exist_ok=True)
os.makedirs(os.path.join(PROJECT_ROOT, "screenshots"), exist_ok=True)
os.makedirs(os.path.join(PROJECT_ROOT, "reports"), exist_ok=True)


class logandscreen:
    _logger = None

    @classmethod
    def _get_logger(cls):
        if cls._logger is None:
            logger = logging.getLogger("MyFramework")
            logger.setLevel(logging.INFO)

            if not logger.handlers:
                log_file = os.path.join(PROJECT_ROOT, "logs", f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
                formatter = logging.Formatter("%(asctime)s | %(levelname)-8s | %(message)s")

                # File handler → saves in ROOT/logs/
                fh = logging.FileHandler(log_file, encoding="utf-8")
                fh.setFormatter(formatter)
                logger.addHandler(fh)

                # Console output
                ch = logging.StreamHandler()
                ch.setFormatter(formatter)
                logger.addHandler(ch)

            cls._logger = logger
        return cls._logger

    @staticmethod
    def info(msg):
        logandscreen._get_logger().info(msg)

    @staticmethod
    def error(msg):
        logandscreen._get_logger().error(msg)

    @staticmethod
    def screenshot(driver, name="fail"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
        screenshot_path = os.path.join(PROJECT_ROOT, "screenshots", f"{name}_{timestamp}.png")
        try:
            driver.save_screenshot(screenshot_path)
            logandscreen._get_logger().error(f"SCREENSHOT SAVED → {screenshot_path}")
        except Exception as e:
            logandscreen._get_logger().error(f"Failed to take screenshot: {e}")




'''
conftest.py → Opens browser, closes browser, takes screenshot on failure, shares tools
utility_tools.py → Writes logs + takes & saves screenshots with one line.'''