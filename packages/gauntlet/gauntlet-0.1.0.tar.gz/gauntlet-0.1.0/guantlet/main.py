import os
import sys
import ast
import time


def check_syntax(file_path):
    try:
        with open(file_path, 'r') as file:
            ast.parse(file.read())
        return True
    except SyntaxError:
        return False


def check_style(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    lines = content.split('\n')
    long_lines = [line for line in lines if len(line) > 100]
    return len(long_lines) == 0


def check_imports(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    tree = ast.parse(content)
    imports = [node for node in ast.walk(tree) if isinstance(node, (ast.Import, ast.ImportFrom))]
    return len(imports) <= 10


def run_gauntlet(directory="."):
    print(f"Running Gauntlet checks on {directory}")
    python_files = [f for f in os.listdir(directory) if f.endswith('.py')]

    for file in python_files:
        file_path = os.path.join(directory, file)
        print(f"\nChecking {file}:")

        print("  Syntax check...", end="")
        time.sleep(0.5)  # Simulate processing time
        if check_syntax(file_path):
            print("PASSED")
        else:
            print("FAILED")

        print("  Style check...", end="")
        time.sleep(0.5)  # Simulate processing time
        if check_style(file_path):
            print("PASSED")
        else:
            print("FAILED (lines > 100 characters)")

        print("  Import check...", end="")
        time.sleep(0.5)  # Simulate processing time
        if check_imports(file_path):
            print("PASSED")
        else:
            print("FAILED (too many imports)")

    print("\nGauntlet run complete!")


def main():
    if len(sys.argv) > 1:
        run_gauntlet(sys.argv[1])
    else:
        run_gauntlet()


if __name__ == "__main__":
    main()