import json
from urllib.request import urlopen

from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel

def get_content(user):
    """Extract text from user dict."""
    country = user["location"]["country"]
    name = f"{user['name']['first']}{user['name']['last']}"
    return f"[b]{name}[/b]\n[green]{country}"

console = Console()

users = json.loads((urlopen("https://randomuser.me/api/?results=30")).read())["results"]
user_renderables = [Panel(get_content(user), expand = True) for user in users]
console.print(Columns(user_renderables))