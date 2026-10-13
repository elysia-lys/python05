import importlib


def main() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print("Checking dependencies:")

    reagents = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
    }

    missing = []

    for name, description in reagents.items():
        try:
            module = importlib.import_module(name)
            version = module.__version__
            print(f"[OK] {name} ({version}) - {description}")
        except ImportError:
            print(f"[MISSING] {name} is not installed")
            missing.append(name)

    print()
    print("pip vs Poetry:")
    print(
        "requirements.txt declares what to install; "
        "pip resolves it at install time."
    )
    print(
        "pyproject.toml declares the same constraints, "
        "and Poetry pins the resolved versions in poetry.lock "
        "so every install is identical."
    )

    if missing:
        print()
        print("Missing reagents detected!")
        print("Install them using pip:")
        print("pip install -r ex0/requirements.txt")
        print("Or install them using Poetry:")
        print("poetry install")
    else:
        print()
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    main()

