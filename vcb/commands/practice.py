"""The practice command."""

import os.path
from random import shuffle

import pandas as pd
from termcolor import colored

from .base import Base


class Practice(Base):
    """practice your current vocab"""

    def run(self):
        vocab_data = pd.read_csv(self.current_vocab_file())
        metadata = pd.read_csv(self.current_vocab_data())
        if not self.options["--ordered"]:
            vocab_data = vocab_data.sample(frac=1)
        if self.options["--no-tones"]:
            vocab_data["tone"] = vocab_data["value"]
            vocab_data["value"] = vocab_data.value.apply(
                lambda s: "".join(l for l in s if not l.isdigit())
            )
        correct = 0
        for _, row in vocab_data.iterrows():
            metadata.loc[metadata.key == row["key"], "times_reviewed"] += 1
            group = metadata.loc[metadata.key == row["key"], "group"].values[0]
            print("Prompt:", colored(row["key"], attrs=["bold"]))
            guess = input()
            if guess == row["value"]:
                metadata.loc[metadata.key == row["key"], "times_correct"] += 1
                if group < 10:
                    metadata.loc[metadata.key == row["key"], "group"] += 1
                correct += 1
                print(colored("Correct!", "green"))
                if self.options["--no-tones"]:
                    print(
                        "With tones its:",
                        colored(self.show_tones(row["tone"]), "yellow"),
                    )
            else:
                metadata.loc[metadata.key == row["key"], "times_incorrect"] += 1
                if group > 1:
                    metadata.loc[metadata.key == row["key"], "group"] -= 1
                print(
                    colored("Incorrect", "red"),
                    "it is",
                    colored(self.show_tones(row["value"]), "red", attrs=["underline"]),
                )
        metadata.to_csv(self.current_vocab_data(), index=False)
        print("Score:", correct, "/", len(vocab_data))
