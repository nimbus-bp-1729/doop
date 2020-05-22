
from collections import namedtuple
from enum import IntFlag
from .constants import Earth

COE = namedtuple("COE", "a e i raan w v")
ID = namedtuple("ID", "launch_year launch_number piece")
Object = namedtuple("Object", "name number classification")

EphemerisType = IntFlag("EphemerisType","SGP SGP4 SDP4 SGP8 SDP8")


SatelliteTLE = namedtuple("SatelliteTLE",
        'object '
        'id '
        'coe '
        'ballistic_coeffecient '
        'bstar '
        'line1 line2'
    )


import attr

@attr.s(slots=True)
class Satelite:
    # name = attr.ib()
    coe = attr.ib(default=None)
    rv = attr.ib(default=None)

    @staticmethod
    def from_tle(tle):
        s = Satellite()
        return s

    @staticmethod
    def from_rv(RV):
        s = Satellite()
        return s

    @staticmethod
    def from_coe(a, e, i, node, w, v, MU=Earth.mu):
        s = Satellite()
        return s


def rv2coe(R, V, mu=Earth.mu):
    """Given postion (R) and velocity (V) in an ECI frame, this returns
    the classical orbital elements: (a, e, i, node, w, v)
    """
    H = np.cross(R,V)

    v = np.linalg.norm(V)
    r = np.linalg.norm(R)
    energy = v*v/2 - mu/r

    E = np.cross(V,H)/mu - R/r
    e = np.linalg.norm(E)

    i = np.arccos(H[2]/np.linalg.norm(H))
    if i < 1e-5: # equitorial orbit
        node = 0
        if e < 1e-5:  # circular
            vv = R[0]/r if R[1] > 0 else 2*pi-R[0]/r
            w = np.NaN
        else: # elliptical
            w = np.arccos(E[0]/e) if E[1] > 0 else 2*pi - np.arccos(E[0]/e)
            vv = np.arccos(np.dot(E,R)/(e*r))
            if np.dot(R,V) < 0:
                vv = 2*pi - vv
    else:
        N = np.cross(np.array([0,0,1]), H)
        n = np.linalg.norm(N)
        node = np.arccos(N[0]/n)
        node = 2*pi-node if N[1] <0 else node
        w = np.arccos(np.dot(N,E)/(d*e))
        w = 2*pi-w if E[2]<0 else w

    return (a, e, i, node, w, v)

def coe2rv(a, e, i, node, w, v, MU=Earth.mu):
    """Given the classical orbital elements (a, e, i, node, w, v), this
    returns the position (R) and the velocity (V) in an ECI frame
    """
    p = a*(1-e*e);  # p = semi-latus rectum
    R = np.zeros(3)
    V = np.zeros(3)
    smup = np.sqrt(MU/p)
    sv = np.sin(v)
    cv = np.cos(v)
    det = 1+e*cv

    # Perifocal
    R(0) =  p*cv/det     # x-coordinate (km)
    R(1) =  p*sv/det     # y-coordinate (km)
    R(2) =  0            # z-coordinate (km)
    V(0) = -smup*sv      # velocity in x (km/s)
    V(1) =  smup*(e+cv)  # velocity in y (km/s)
    V(2) =  0            # velocity in z (km/s)

    # R313 = Z1X2Z3 = https://en.wikipedia.org/wiki/Euler_angles
    #rot = rot3(-node)*rot1(-i)*rot3(-arg);
    s3 = np.sin(n); c3 = np.cos(n)
    s2 = np.sin(i); c2 = np.cos(i)
    s1 = sv; c1 = cv
    R313 = np.array(
        [
            [c1*c3-c2*s1*s3, -c1*s3-c2*c3*s1, s1*s2],
            [c3*s1+c1*c2*c3, c1*c2*s3, c1*c2*c3-s1*s3,-c1*s2],
            [s2*s3, c3*s2, c2]
        ]
    )

    # Perifocal -> xyz
    R = R313.dot(R)
    V = R313.dot(V)

    return (R,V,)
