import os
from argparse import ArgumentParser
from importlib import import_module

def main() -> None:
    parser = ArgumentParser(description="Just another Python exercise.")
    parser.add_argument("exercise", choices=['project_euler'])
    parser.add_argument("number", type=int)
    args = parser.parse_args()

    result = run(args.exercise, args.number)
    if not result:
        print(f"Couldn't find solution for {args.exercise} exercise number {args.number}.")


def run(exercise: str, num: int) -> bool:
    print(f"Exercise: {exercise}")
    print(f"Number:   {num}")

    current_dir = os.path.dirname(__file__)
    module_dir = os.path.join(current_dir, exercise)
    if not os.path.exists(os.path.join(module_dir, '__init__.py')):
        return False
    
    module_prefix = f'problem_{num:04d}'
    module_name = None
    try:
        for filename in os.listdir(module_dir):
            if filename.startswith(module_prefix) and filename.endswith('.py'):
                module_name = filename[:-3]
                break
    except Exception as e:
        print(f"Couldn't find module with prefix {module_prefix} in directory {module_dir}: {e}")
        return False
    if module_name is None:
        return False

    try:
        module_path = f'{exercise}.{module_name}'
        module = import_module(module_path)
        print("Solution:")
        module.solution()
    except ImportError as e:
        print(f"Couldn't import module {module_path}: {e}")
        return False
    return True


if __name__ == '__main__':
    main()
