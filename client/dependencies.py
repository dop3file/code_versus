from rich import pretty
from rich.console import Console, Theme, Style


pretty.install()
custom_theme = Theme({
    "info": "bold magenta",
    "warning": "bold yellow",
    "error": "bold red",
    "success": "bold green",
    "easy": "bold green",
    "medium": "bold yellow",
    "hard": "bold red",
    "True": "bold green",
    "False": "bold red"
})
console = Console(theme=custom_theme)