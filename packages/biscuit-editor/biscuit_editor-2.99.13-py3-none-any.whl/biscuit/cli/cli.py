import os
import sys
from pathlib import Path

import click

from biscuit import __version__, get_app_instance

from . import editor, extensions, git  # reason: see at bottom


@click.group(invoke_without_command=True)
@click.version_option(__version__, "-v", "--version", message="Biscuit v%(version)s")
@click.help_option("-h", "--help")
@click.option("--dev", is_flag=True, help="Run in development mode")
def cli(path=None, dev=False):
    """Biscuit CLI"""

    click.echo(f"Biscuit v{__version__} {'(dev) 🚧' if dev else '🚀'}")


@cli.result_callback()
@click.pass_context
def process_commands(context: click.Context, processors, path=None, dev=False):
    """Process the commands"""

    if path:
        path = str(Path(path).resolve())
        click.echo(f"Opening {path}")

    appdir = Path(os.path.abspath(__file__)).parent
    app = get_app_instance(appdir, open_path=path)

    if processors:
        if isinstance(processors, list):
            for processor in processors:
                processor(app)
        else:
            processors(app)

    app.run()


@cli.command("doc")
def docs():
    """Open the documentation"""

    click.launch("https://tomlin7.github.io/biscuit/")
    exit()


def setup():
    """Setup the CLI commands"""

    extensions.register(cli)
    git.register(cli)
    editor.register(cli)


def run():
    """Run the CLI"""

    setup()
    cli()


if __name__ == "__main__":
    run()
