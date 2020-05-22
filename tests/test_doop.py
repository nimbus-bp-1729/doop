import doop
from doop.tle import parse_tle

def test_tle():
    tle = """ISS (ZARYA)
    1 25544U 98067A   20060.61908565  .00000737  00000-0  21434-4 0  9993
    2 25544  51.6436 165.6500 0005418 332.6966 228.1099 15.49204316215186"""

    s = parse_tle(tle)
    assert s.object.name == "ISS (ZARYA)"
    assert s.object.number == 25544
    assert s.object.classification == "Unclassified"
