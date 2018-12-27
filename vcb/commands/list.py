"""The list command."""

import os

from termcolor import colored

from .base import Base


class List(Base):
    """set the current vocab"""

    def run(self):
        vocabs = filter(lambda v: v != "vocab.conf", os.listdir(self.vocab_dir))
        for vocab in vocabs:
            if vocab == self.current_vocab():
                print(colored(vocab, "green"), "<- current vocab")
            else:
                print(vocab)
