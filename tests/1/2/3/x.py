from pathlib import Path

from utils.functions import get_project_root

current = Path(__file__).resolve()
print(current)

print(get_project_root(custom_marker='tests'))