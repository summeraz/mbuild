import numpy as np

import mbuild as mb


class Ester(mb.Compound):
    """A ester group -C(=O)O-. """
    def __init__(self):
        super(Ester, self).__init__()

        mb.load('ester.pdb', compound=self, relative_to_module=self.__module__)
        self.translate(-self[0].pos)

        up_port = mb.Port(anchor=self[2], orientation=[1, 0, 0],
                          separation=0.07, label='up')
        down_port = mb.Port(anchor=self[0], orientation=[-1, 0, 0],
                            separation=0.07, label='down')

if __name__ == '__main__':
    m = Ester()
    m.save('ester.mol2', overwrite=True)
