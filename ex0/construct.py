import os
import sys
import site


def main() -> None:
    print("LABORATORY STATUS: ", end="")

    if sys.prefix != sys.base_prefix:
        print("The laboratory is sealed\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting the global system\n")
        print("Readent intallation path:")
        print(site.getsitepackages()[0])
    else:
        print("You are working in the open\n")
        print(f"Current Python: {sys.executable}.{sys.version_info.minor}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.\n")
        print("To seal the laboratory, run: ")
        print("python3 -m venv lab_env")
        print("source lab-env/bin/activate # On Unix")
        print("lab_env\\Scripts\\activate # On Windows")
        print("\nThen run this program again.")


if __name__ == "__main__":
    main()
