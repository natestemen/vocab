"""The create command."""

import csv
import os

from ruamel.yaml import YAML

from .base import Base


class Create(Base):
    """do some required setup for a new vocab set"""

    def run(self):
        yaml = YAML()
        if not os.path.isdir(self.vocab_dir):
            os.mkdir(self.vocab_dir)
            with open(self.vocabrc, "x") as f:
                yaml.dump({"current_vocab": None}, f)
        new_vocab_file = os.path.join(self.vocab_dir, self.options["<name>"])
        if not os.path.isfile(new_vocab_file):
            with open(new_vocab_file, "x") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(["key", "value"])
            self.update_current_vocab()
        else:
            print(
                "You already have a vocab under that name please try "
                "another name or switch to that vocab and add to that."
            )
