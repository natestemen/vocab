"""The use command."""


import os.path

from termcolor import colored

from .base import Base


class Use(Base):
    """set the current vocab"""

    def run(self):
        vocab_directory = self.vocab_dir
        new_vocab_file = os.path.join(vocab_directory, self.options["<name>"])
        if not os.path.isfile(new_vocab_file):
            print(
                "You do not have that vocab file yet.\n"
                "Use vcb create {} to generate it.".format(self.options["<name>"])
            )
            return
        self.update_current_vocab()