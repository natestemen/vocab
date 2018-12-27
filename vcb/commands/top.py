"""The top command."""

from ruamel.yaml import YAML
import csv
import pandas as pd
import os.path
from .base import Base


class Top(Base):
    """set the current vocab"""

    def run(self):
        vocab_file = self.current_vocab_file()
        with open(vocab_file) as f:
            dat = pd.read_csv(f)
        idx = int(self.options['--number']) if self.options['--number'] else 10
        print(dat[['key', 'value']][:idx].to_string(index=False))