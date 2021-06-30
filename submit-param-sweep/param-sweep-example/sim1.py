#!/usr/bin/env python

#                     R
#           ---------www--------
#          |                    |
#          |                    |
#         _|_                   |
#        |   |                  |
#        | + |               -------
#  Vin   | - |               -------   C
#        |___|                  |
#          |                    |
#          |                    |
#          |                    |
#           --------------------
#                     |
#                   -----
#                    ---
#                     -

import optparse
import ConfigParser
import numpy as np


def vc(Vin,R,C,lowerbound,upperbound):
    """Calculate the voltage across the capacitor
    """

    if lowerbound == upperbound:
        npts = 1
    else:
        npts = 100

    t = np.linspace(lowerbound,upperbound,npts)
    v = Vin*(1-np.exp(-t/(R*C)))

    return t,v


def parseoptions():
    parser = optparse.OptionParser()

    parser.add_option('--Vin',
                      help='Input voltage to the system with units of volts (V)',
                      action="store",
                      dest="Vin",
                      default=10.0,
                      type="float")

    parser.add_option('--R',
                      help='Impedance of the resistor with units of ohms',
                      action="store",
                      dest="R",
                      default=100e3,
                      type="float")

    parser.add_option('--C',
                      help='Capacitance of the capacitor with units of farads (F)',
                      action="store",
                      dest="C",
                      default=100e-6,
                      type="float")

    parser.add_option('--lowerbound',
                      help='Lower bound of the time frame to examine with units of seconds (s)',
                      action="store",
                      dest="lb",
                      default=0.0,
                      type="float")

    parser.add_option('--upperbound',
                      help='Upper bound of the time frame to examine with units of seconds (s)',
                      action="store",
                      dest="ub",
                      default=60.0,
                      type="float")

    parser.add_option('--log',
                      help='Name of the file used to store results',
                      action="store",
                      dest="log",
                      default='out.log',
                      type="string")

    parser.add_option('--inputdeck',
                      help='read input values from an ini style configuration' \
                           + ' file, this overrides command line options',
                      action="store",
                      dest="inputdeck",
                      default=None,
                      type="string")

    options,remainder = parser.parse_args()
    return options,remainder


if __name__=='__main__':

    options,remainder = parseoptions()

    Vin = options.Vin
    R = options.R
    C = options.C
    lb = options.lb
    ub = options.ub


    if options.inputdeck is not None:
        # override command line options with values from
        # a configuration file

        defaults = {
            'Vin' : str(Vin),
            'R'   : str(R),
            'C'   : str(C),
            'lb'  : str(lb),
            'ub'  : str(ub),
        }

        c = ConfigParser.ConfigParser(defaults)
        c.read(options.inputdeck)

        Vin = float(c.get('inputs','Vin'))
        R   = float(c.get('inputs','R'))
        C   = float(c.get('inputs','C'))
        lb  = float(c.get('inputs','lb'))
        ub  = float(c.get('inputs','ub'))


    # run the simulation

    t,v = vc(Vin,R,C,lb,ub)

    with open(options.log,'w') as f:
        for n in zip(t,v):
            print >> f, "%g %g" % n

