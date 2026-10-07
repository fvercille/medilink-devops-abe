import compileall
import subprocess
import sys


def main():
    print("--- Running Syntax Check ---")
    if not compileall.compile_dir(".", force=True, quiet=True):
        print("Syntax compilation failed!")
        return 1

    print("--- Running Unit Tests ---")
    result = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"])
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())