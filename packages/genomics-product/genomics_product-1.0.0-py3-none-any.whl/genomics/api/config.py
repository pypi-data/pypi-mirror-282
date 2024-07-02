from __future__ import annotations

from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel
from pydantic import SecretStr

CONFIG_PATH = Path.home().joinpath(".genomics").joinpath("config")


class APIConfig(BaseModel):
    backend_url: str
    # rt_url: str
    access_token: SecretStr


class GenomicsConfig(BaseModel):
    api_config: APIConfig
    version: Optional[str]

    @classmethod
    def from_yaml_file(cls, config_file: Path) -> GenomicsConfig:
        with open(config_file, encoding="utf-8") as f:
            yaml_config = yaml.safe_load(f)

        return cls(**yaml_config)

    @classmethod
    def load_config(cls,
                    config_file: Path = CONFIG_PATH / "config.yaml") -> GenomicsConfig:
        return cls.from_yaml_file(config_file)

    def save_config(self, config_file: Path = CONFIG_PATH / "config.yaml") -> None:
        self.to_yaml_file(config_file)

    def to_yaml_file(self, config_file: Path) -> None:
        try:
            # create the directory if it doesn't exist
            config_file.parent.mkdir(parents=True, exist_ok=True)

            config = self.dict()

            # by default the access token is a SecretStr, which hides the token value for
            # safety reasons we need to convert it to a string before saving to yaml
            config["api_config"]["access_token"] = \
                config["api_config"]["access_token"].get_secret_value()

            with config_file.open("w") as f:
                yaml.safe_dump(config, f)
        except PermissionError as e:
            print(
                f"Permission error: You don't have the necessary permissions to write to "
                f"'{config_file}'. Error details: {e}")

        except (IOError, OSError) as e:
            print(f"File system error occurred: {e}")

        except yaml.YAMLError as e:
            print(f"Error while dumping data to YAML: {e}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
