import os
import ollama
from rich import print
from get_gitlab_issues import check_access
from .config import CACHE_FILE


def check_gitlab_credentials(token, url):
    if not check_access(token, url):
        print(f"[red]Invalid GitLab credentials[/red]")
        raise Exception("Invalid GitLab credentials")
    print("[green]GitLab credentials are valid[/green]")


def check_ollama(model=None):
    try:
        models = ollama.list()['models']
        if models and not any(m['name'] == model for m in models):
            print(f"[red]Invalid Ollama model[/red]")
            raise Exception("Invalid Ollama model")
    except Exception as e:
        print(f"[red]Ollama is not running. Error: {e}[/red]")
        raise Exception("Ollama is not running")
    print("[green]Ollama model is valid[/green]")


def manage_cache_file(create=False, content=None):
    if create:
        with open(CACHE_FILE, 'w') as f:
            f.write(content)
    else:
        if os.path.exists(CACHE_FILE):
            os.remove(CACHE_FILE)