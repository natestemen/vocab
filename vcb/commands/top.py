"""The top command."""

import csv
import os.path

import pandas as pd
from ruamel.yaml import YAML

from .base import Base


class Top(Base):
    """set the current vocab"""

    def run(self):
        vocab_file = self.current_vocab_file()
        with open(vocab_file) as f:
            dat = pd.read_csv(f)
        idx = int(self.options["--number"]) if self.options["--number"] else 10
        print(dat[["key", "value"]][:idx].to_string(index=False))
