"""The status command."""


from ruamel.yaml import YAML
import os.path
from termcolor import colored
from .base import Base


class Status(Base):
    """set the current vocab"""

    def run(self):
        yaml = YAML()
        if not os.path.isfile(self.vocabrc):
            print('You have not yet set up any vocab sets. ' \
                  'Use', colored('vcb create <name>', 'green'), 'to create one.')
            return
        with open(self.vocabrc) as f:
            dat = yaml.load(f)
        print('Current vocab is set to', dat['current_vocab'])