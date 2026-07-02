from pathlib import Path

# Root Directory
ROOT_DIR = Path(__file__).resolve().parent.parent

# Data
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
CACHE_DIR = DATA_DIR / "cache"

# Models
MODEL_DIR = ROOT_DIR / "models"
FAISS_DIR = MODEL_DIR / "faiss"

# Outputs
OUTPUT_DIR = ROOT_DIR / "outputs"

# Logs
LOG_DIR = ROOT_DIR / "logs"