from __future__ import division

import numpy as np

import mbuild as mb


class C3(mb.Compound):
    """A tri-valent, planar carbon."""
    def __init__(self):
        super(C3, self).__init__(name='C')

        up_port = mb.Port(anchor=self, orientation=[0, 1, 0],
                          separation=0.07, label='up')
        down_port = mb.Port(anchor=self, orientation=[-0.866, -0.5, 0],
                            separation=0.07, label='up')
        left_port = mb.Port(anchor=self, orientation=[0.866, -0.5, 0],
                            separation=0.07, label='up')

if __name__ == '__main__':
    m = C3()
    m.save('c3.mol2',overwrite=True)
