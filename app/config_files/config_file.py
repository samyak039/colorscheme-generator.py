from dataclasses import dataclass


@dataclass
class ConfigFile:
    name: str
    ext: str
    url: str
    template: str
