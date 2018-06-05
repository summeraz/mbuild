import numpy as np

import mbuild as mb


class H(mb.Compound):
    """A hydrogen atom with two overlayed ports."""
    def __init__(self):
        super(H, self).__init__(name='H')

        up_port = mb.Port(anchor=self, orientation=[0, 1, 0],
                          separation=0.07, label='up')

if __name__ == '__main__':
    m = H()
    m.save('h.mol2', overwrite=True)
