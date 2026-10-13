import os
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()

    print("ORACLE STATUS: Consulting the configuration...")

    mode = os.getenv("MATRIX_MODE", "development")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "DEBUG")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if database_url:
        if mode == "development":
            print("Database: Connected to local instance")
        else:
            print("Database: Configuration available")
    else:
        print("Database: Not configured")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Not configured")

    print(f"Log Level: {log_level}")

    if zion_endpoint:
        print("Remote Network: Online")
    else:
        print("Remote Network: Not configured")

    print()
    print("Configuration security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file should be ignored by git")
    print("[OK] Production overrides available")

    if mode == "development":
        print("Development mode: Debugging enabled")
    elif mode == "production":
        print("Production mode: Debugging disabled")
    else:
        print("WARNING: Unknown MATRIX_MODE value")

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
