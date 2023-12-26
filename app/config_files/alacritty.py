from ..colorschemes import Colorscheme
from .config_file import ConfigFile

ALACRITTY = ConfigFile(
    name="alacritty",
    ext="yml",
    url="https://github.com/alacritty/alacritty",
    template=f"""
# Alacritty Colors
colors:
  # Default colors
  primary:
    background: '{Colorscheme.dark0}'
    foreground: '{Colorscheme.light0}'
    """,
)
