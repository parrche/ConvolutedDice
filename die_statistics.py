import numpy as np
from collections import Counter


class DieSample:
    """A class for generating samples of dice rolls"""

    def __init__(self, die_list=(6, 6), sample_size: int = 1000):
        self.die_list = die_list
        self.sample_size = sample_size

        # calculate event space
        self.events = np.arange(len(die_list), sum(die for die in die_list)+1)

        # initialize sample
        self.rolls = np.zeros(sample_size, dtype=np.int32)

        # call method to generate sample
        self.generate_sample()

    def generate_sample(self):
        """Perform dice rolls to generate sample"""
        for die in self.die_list:
            self.rolls += np.random.randint(low=1, high=die+1, size=self.sample_size)

    @property
    def frequencies(self) -> np.ndarray:
        """Count frequencies"""
        freq_dict = Counter(self.rolls)
        return [freq_dict[event] for event in self.events]
