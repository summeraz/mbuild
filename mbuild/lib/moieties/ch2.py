import mbuild as mb


class CH2(mb.Compound):
    """A methylene bridge. """
    def __init__(self):
        super(CH2, self).__init__()

        mb.load('ch2.pdb', compound=self, relative_to_module=self.__module__)
        self.translate(-self[0].pos)  # Move carbon to origin.

        up_port = mb.Port(anchor=self[0], orientation=[0, 1, 0],
                          separation=0.07, label='up')
        down_port = mb.Port(anchor=self[0], orientation=[0, -1, 0],
                            separation=0.07, label='down')

if __name__ == '__main__':
    ch2 = CH2()
    ch2.save('ch2.mol2')
