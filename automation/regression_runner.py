
# execute all firmware validation suites
# provide one command for full regression testing


import subprocess
import sys


# run full pytest regression suite
def run_regression():
    result = subprocess.run(
        [sys.executable, "-m", "pytest"],
        check=False,
    )

    return result.returncode


# start regression runner from command line
def main():
    exit_code = run_regression()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()