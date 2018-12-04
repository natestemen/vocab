"""The status command."""


from ruamel.yaml import YAML

import os.path

from .base import Base


class Status(Base):
    """set the current vocab"""

    def run(self):
        yaml = YAML()
        home_directory = os.path.expanduser('~')
        vocab_directory = os.path.join(home_directory, '.vocab')
        vocabrc_file = os.path.join(vocab_directory, 'vocab.conf')
        if not os.path.isfile(vocabrc_file):
            print('You have not yet set up any vocab sets. ' \
                  'Use vcb create <name> to create one')
        with open(vocabrc_file) as f:
            dat = yaml.load(f)
        print('Current vocab is set to', dat['current_vocab'])