from collections import namedtuple
from math import pi

# value?
femto = 1E-15
pico = femto*1000
nano = pico*1000
micro = nano*1000
milli = micro*1000
centi = 1E-2
kilo = 1E3
mega = kilo*1000
giga = mega*1000

# conversions
deg2rad = pi/180
rad2deg = 180/pi

# https://en.wikipedia.org/wiki/Earth
# radius [km]
# mass [kg]
# standard gravitational const [m^3/sec^2]
# tilt [deg]
Body = namedtuple("Body", "radius mass mu tilt")

Earth = Body(6378.388, 5.97237E24, 3.986004418E14, 23.4392811)
