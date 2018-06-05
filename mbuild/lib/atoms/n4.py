import mbuild as mb
import numpy as np


class N4(mb.Compound):
    """An tetravalent nitrogen atom."""
    def __init__(self):
        super(N4, self).__init__(name='N')

        port0 = mb.Port(anchor=self, label='port[$]')
        port1 = mb.Port(anchor=self, label='port[$]')
        port2 = mb.Port(anchor=self, label='port[$]')
        port3 = mb.Port(anchor=self, label='port[$]')

        self['port[2]'].spin(2/3*np.pi, [1, 0, 0])
        self['port[3]'].spin(-2/3*np.pi, [1, 0, 0])
        self['port[1]'].spin(1/3*np.pi, [0, 0, 1])
        self['port[2]'].spin(-1/3*np.pi, [0, 0, 1])
        self['port[3]'].spin(-1/3*np.pi, [0, 0, 1])

        self['port[0]'].translate([0, 0.073, 0])
        self['port[1]'].translate([0.0594, -0.0243, 0])
        self['port[2]'].translate([-0.042, -0.0243, 0.042])
        self['port[3]'].translate([-0.042, -0.0243, -0.042])


if __name__ == '__main__':
    m = N4()
    m.save('n4.mol2', overwrite=True)
