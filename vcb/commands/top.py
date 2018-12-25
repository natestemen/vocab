"""The top command."""

from ruamel.yaml import YAML
import csv
import pandas as pd
import os.path
from .base import Base


class Top(Base):
    """set the current vocab"""

    def run(self):
        yaml = YAML()
        home_directory = os.path.expanduser('~')
        vocab_directory = os.path.join(home_directory, '.vocab')
        vocabrc_file = os.path.join(vocab_directory, 'vocab.conf')
        with open(vocabrc_file) as f:
            current_vocab = yaml.load(f)['current_vocab']
        vocab_file = os.path.join(vocab_directory, current_vocab)
        with open(vocab_file) as f:
            dat = pd.read_csv(f)
        idx = int(self.options['--number']) if self.options['--number'] else 10
        print(dat[['key', 'value']][:idx].to_string(index=False))