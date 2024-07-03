import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

PYTOOLBELT_TOOL_CONFIGS_PATH = Path.home() / ".pytoolbelt" / "configs"


def get_config_path() -> Path:
    tool_name = Path(sys.argv[0]).name
    return PYTOOLBELT_TOOL_CONFIGS_PATH / f"{tool_name}.yml"


TOOL_CONFIG_FILE = "config.yml"


@dataclass
class PtVenvConfig:
    name: str
    version: str


@dataclass
class ToolConfig:
    name: str
    version: str
    ptvenv: PtVenvConfig

    @classmethod
    def from_file(cls) -> "ToolConfig":
        with open(TOOL_CONFIG_FILE, "r") as f:
            config = yaml.safe_load(f)["tool"]

        return cls(
            name=config["name"],
            version=config["version"],
            ptvenv=PtVenvConfig(
                name=config["ptvenv"]["name"],
                version=config["ptvenv"]["version"],
            ),
        )
