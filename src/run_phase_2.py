import sys
from pathlib import Path

# Add project root to sys.path to allow imports from src
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.models.train_model import main  # noqa: E402

if __name__ == "__main__":
    print(f"Running Modeling from {PROJECT_ROOT}...")
    main()
