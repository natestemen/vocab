"""
vcb

Usage:
  vcb create <name>
  vcb use <name>
  vcb add <key> <value>
  vcb status
  vcb practice [--reverse|--both] [--ordered] [--no-tones]
  vcb top [--number=<num>]
  vcb -h | --help
  vcb --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  vcb create spanish
  vcb add hello hola
  vcb use mandarin

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/natestemen/vocab
"""


from inspect import getmembers, isclass
from docopt import docopt
from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import vcb.commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for k, v in options.items(): 
        if hasattr(vcb.commands, k) and v:
            module = getattr(vcb.commands, k)
            vcb.commands = getmembers(module, isclass)
            command = [command[1] for command in vcb.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
