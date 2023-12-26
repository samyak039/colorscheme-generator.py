from dataclasses import dataclass


@dataclass
class Colorscheme:
    dark0_hard: str
    dark0: str
    dark0_soft: str
    dark1: str
    dark2: str
    dark3: str
    dark4: str

    gray_faded: str
    gray_bright: str

    light0_hard: str
    light0: str
    light0_soft: str
    light1: str
    light2: str
    light3: str
    light4: str

    bright_red: str
    bright_green: str
    bright_yellow: str
    bright_blue: str
    bright_purple: str
    bright_aqua: str
    bright_orange: str

    neutral_red: str
    neutral_green: str
    neutral_yellow: str
    neutral_blue: str
    neutral_purple: str
    neutral_aqua: str
    neutral_orange: str

    faded_red: str
    faded_green: str
    faded_yellow: str
    faded_blue: str
    faded_purple: str
    faded_aqua: str
    faded_orange: str
