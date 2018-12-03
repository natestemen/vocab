"""The create command."""

from ruamel.yaml import YAML

import os

from .base import Base


class Create(Base):
    """do some required setup for a new vocab set"""

    def run(self):
        yaml = YAML()
        home_directory = os.path.expanduser('~')
        vocab_directory = os.path.join(home_directory, '.vocab')
        vocabrc_file = os.path.join(vocab_directory, 'vocab.conf')
        if not os.path.isdir(vocab_directory):
            os.mkdir(vocab_directory)
            with open(vocabrc_file, 'x') as f:
                yaml.dump({'current_vocab': None}, f)
        new_vocab_file = os.path.join(vocab_directory, self.options['<name>'])
        if not os.path.isfile(new_vocab_file):
            open(new_vocab_file, 'x').close()
            with open(vocabrc_file) as f:
                vocabrc = yaml.load(f)
            vocabrc['current_vocab'] = self.options['<name>']
            with open(vocabrc_file, 'w') as f:
                yaml.dump(vocabrc, f)
            print('Your vocab path has been set to', new_vocab_file)
        else:
            print('You already have some vocab under that name please try ' \
                  'another name or add vocab to that file')