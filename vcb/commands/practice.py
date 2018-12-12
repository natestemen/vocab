"""The practice command."""

import csv

from ruamel.yaml import YAML

import os.path

from .base import Base

class Practice(Base):
    """practice your current vocab"""

    def run(self):
        yaml = YAML()
        home_directory = os.path.expanduser('~')
        vocab_directory = os.path.join(home_directory, '.vocab')
        vocabrc_file = os.path.join(vocab_directory, 'vocab.conf')
        with open(vocabrc_file) as f:
            current_vocab = yaml.load(f)['current_vocab']
        vocab_file = os.path.join(vocab_directory, current_vocab)
        with open(vocab_file) as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row['key'])
                guess = input()
                if guess == row['value']:
                    continue
                else:
                    print('sorry, it was', row['value'])