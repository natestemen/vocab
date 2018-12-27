"""The practice command."""

import os.path
from random import shuffle

import pandas as pd
from termcolor import colored

from .base import Base


class Practice(Base):
    """practice your current vocab"""

    def run(self):
        with open(self.current_vocab_file()) as f:
            vocab_data = pd.read_csv(f)
        if not self.options["--ordered"]:
            vocab_data = vocab_data.sample(frac=1)
        if self.options["--no-tones"]:
            vocab_data["tone"] = vocab_data["value"]
            vocab_data["value"] = vocab_data.value.apply(
                lambda s: "".join(l for l in s if not l.isdigit())
            )
        correct = 0
        for _, row in vocab_data.iterrows():
            print("Prompt:", colored(row["key"], attrs=["bold"]))
            guess = input()
            if guess == row["value"]:
                correct += 1
                print(colored("Correct!", "green"))
                if self.options["--no-tones"]:
                    print("With tones its:", colored(row["tone"], "yellow"))
            else:
                print(
                    colored("Incorrect", "red"),
                    "it is",
                    colored(row["value"], "red", attrs=["underline"]),
                )
        print("Score:", correct, "/", len(vocab_data))
