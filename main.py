import logging
import os
import subprocess

_logger = logging.getLogger(__name__)


def process_data(data: str) -> str:
    """Processes string data safely."""
    _logger.info("Processing: %s", data.upper())
    return data


def run_safe_command(user_input: str) -> None:
    """Runs a shell command safely using a list."""
    # Use full path to executable to satisfy S607
    subprocess.run(["/usr/bin/ls", user_input], check=False)


def database_connect() -> None:
    """Connects to a database using environment variables."""
    api_key = os.getenv("DB_API_KEY", "default_key")
    _logger.info("Connecting with API Key: %s", api_key)


def calculate_sum(a: int, b: int, c: int) -> int:
    """Calculates the sum of three integers."""
    result = a + b + c
    if result > 10:
        _logger.info("Result is large")
    return result


if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Test all functions
    process_data("Correct Data String")
    run_safe_command(".")
    database_connect()

    x, y, z = 10, 20, 30
    total = calculate_sum(x, y, z)
    _logger.info("Total: %d", total)
