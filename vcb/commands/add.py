"""The add command."""


import csv
import os.path
from datetime import datetime

import pandas as pd
from termcolor import colored

from .base import Base


class Add(Base):
    """add a word/sentence to your current vocab list"""

    def run(self):
        vocab_file = self.current_vocab_file()
        data_file = self.current_vocab_data()
        key = self.options["<key>"]
        value = self.options["<value>"]
        with open(vocab_file) as f:
            vocab_data = pd.read_csv(f)
        if key in vocab_data.key.values:
            print(colored("Sorry, you already have that key in your vocab", "red"))
            print(
                colored(
                    "{} <-> {} already exists. Keys and values must be unique".format(
                        key,
                        self.show_tones(
                            vocab_data[vocab_data.key == key].value.values[0]
                        ),
                    ),
                    "yellow",
                )
            )
            return
        with open(vocab_file, "a") as f:
            writer = csv.writer(f)
            writer.writerow([key, value])
        metadata = pd.read_csv(data_file)
        metadata = metadata.append(
            {
                "key": key,
                "value": value,
                "date_added": datetime.now(),
                "times_reviewed": 0,
                "times_correct": 0,
                "times_incorrect": 0,
                "group": 0,
            },
            ignore_index=True,
        )
        metadata.to_csv(data_file, index=False)
        print(
            "{} <-> {} has been added to your vocab".format(key, self.show_tones(value))
        )
