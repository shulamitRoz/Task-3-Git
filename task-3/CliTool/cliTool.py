import json
from pathlib import Path
import typer

app = typer.Typer()
file_path = Path("data.json")

@app.command()
def append_json(item: str):
    """Append a valid JSON argument to the local file."""
    try:
        parsed_item = json.loads(item)  # מוודא שהקלט הוא JSON תקין
    except json.JSONDecodeError:
        typer.echo("Error: Invalid JSON format.")
        raise typer.Exit(code=1)

    data = []
    if file_path.exists():
        with open(file_path, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                typer.echo("Warning: Existing file is corrupted. Overwriting.")
                data = []

    data.append(parsed_item)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)
    typer.echo(f"Added: {parsed_item}")

@app.command()
def show_last():
    """Show the last 10 JSON arguments from the persisted file."""
    if not file_path.exists():
        typer.echo("No data found:)")
        raise typer.Exit()

    with open(file_path, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            typer.echo("Error: Data file is corrupted.")
            raise typer.Exit(code=1)

    for item in data[-10:]:
        typer.echo(json.dumps(item, indent=2))

if __name__ == "__main__":
    app()
