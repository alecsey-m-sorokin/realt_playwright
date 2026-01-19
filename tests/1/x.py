from pathlib import Path

base_dir = Path(__file__).resolve().parent
print(base_dir)
root_dir = Path(__file__).resolve().parents[2]
print(root_dir)
