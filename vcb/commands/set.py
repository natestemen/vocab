"""The set command."""


from json import dumps

from .base import Base


class Set(Base):
    """do some required setup"""

    def run(self):
        self.vocab_path = self.options['<path>']
        print('Your vocab path has been set to ', self.vocab_path)