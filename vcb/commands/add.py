"""The add command."""


from ruamel.yaml import YAML

import os.path

import csv

from .base import Base


class Add(Base):
    """add a word/sentence to your current vocab list"""

    def run(self):
        yaml = YAML()
        key = self.options['<key>']
        value = self.options['<value>']
        home_directory = os.path.expanduser('~')
        vocab_directory = os.path.join(home_directory, '.vocab')
        vocabrc_file = os.path.join(vocab_directory, 'vocab.conf')
        with open(vocabrc_file) as f:
            current_vocab = yaml.load(f)['current_vocab']
        vocab_file = os.path.join(vocab_directory, current_vocab)
        with open(vocab_file, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([key, value])
        print('{} <-> {} has been added to your vocab'.format(key, value))