__author__ = 'jonestj1'

import mbuild as mb

class PegMonomer(mb.Compound):
    def __init__(self):
        super(PegMonomer, self).__init__()

        mb.load('peg_monomer.pdb', compound=self, relative_to_module=self.__module__)
        self.translate(-self[0].pos)

        down_port = mb.Port(anchor=self[0], orientation=[0, -1, 0],
                            separation=0.07, label='down')
        up_port = mb.Port(anchor=self[6], orientation=[0, 1, 0],
                          separation=0.073, label='up')

if __name__ == '__main__':
    peg = PegMonomer()
    peg.save('peg.mol2')
