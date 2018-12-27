"""The status command."""


import os.path

from termcolor import colored

from .base import Base


class Status(Base):
    """set the current vocab"""

    def run(self):
        if not os.path.isfile(self.vocabrc):
            print(
                "You have not yet set up any vocab sets. " "Use",
                colored("vcb create <name>", "green"),
                "to create one.",
            )
            return
        print("Current vocab is set to {}.".format(colored(self.current_vocab(), "green")))
