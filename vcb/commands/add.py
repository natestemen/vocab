"""The add command."""


from ruamel.yaml import YAML
import os.path
from datetime import datetime
import csv
import pandas as pd
from termcolor import colored
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
        with open(vocab_file) as f:
            vocab_data = pd.read_csv(f)
        if key in vocab_data.key.values:
            print(colored('Sorry, you already have that key in your vocab', 'red'))
            print(colored('{} <-> {} already exists. Keys and values must be unique'.format(key, vocab_data[vocab_data.key == key].value[0]), 'yellow'))
            return
        with open(vocab_file, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([key, value, datetime.now()])
        print('{} <-> {} has been added to your vocab'.format(key, value))