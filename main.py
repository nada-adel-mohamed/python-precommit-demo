import os
import subprocess


def process_data(data: str) -> str:
    """Processes string data safely."""
    print(f"Processing: {data.upper()}")
    return data


def run_safe_command(user_input: str) -> None:
    """Runs a shell command safely using a list."""
    subprocess.run(["ls", user_input], check=False)


def database_connect() -> None:
    """Connects to a database using environment variables."""
    api_key = os.getenv("DB_API_KEY", "default_key")
    print(f"Connecting with API Key: {api_key}")


def calculate_sum(a: int, b: int, c: int) -> int:
    """Calculates the sum of three integers."""
    result = a + b + c
    if result > 10:
        print("Result is large")
    return result


if __name__ == "__main__":
    # Test all functions
    process_data("Correct Data String")
    run_safe_command(".")
    database_connect()

    x, y, z = 10, 20, 30
    total = calculate_sum(x, y, z)
    print(f"Total: {total}")
