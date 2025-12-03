import yaml
from pathlib import Path
from config.schema import Config

def load_config(config_path: str) -> Config:
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    with open(path, "r", encoding="utf-8") as f:
        config_data = yaml.safe_load(f)
    
    return Config(**config_data)
