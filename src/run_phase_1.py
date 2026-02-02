import sys
from pathlib import Path

# Add project root to sys.path to allow imports from src
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.data.make_dataset import main  # noqa: E402

if __name__ == "__main__":
    print(f"Running Data Engineering from {PROJECT_ROOT}...")
    main()
