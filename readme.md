![](pics/zapp.png)

# DOOP

**Still figuring out what I want to do with this**

## Documents

### Two Line Elements ([TLEs](docs/tle/tle.md))

```
TBD
```

### Classical Orbital Elements

![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Orbit1.svg/266px-Orbit1.svg.png)

- Semimajor-axis (a): orbit size
- Eccentricity (e): orbit shape
- Inclination (i): orbital plane inclination measure from ascending node
- Arg of Perigee ($\omega$): orbit orientation
- Ascending Node ($\Omega$): location of assending node
- True Anomaly (v): location of satellite in orbit relative to perigee
- Mean Anomaly (M): fictitious angle that varies linearly with time

## Other Useful Packages

- [spaceman3D](https://github.com/Jaseibert/spaceman3D) reading tles, plotting, appears dead, don't think it works correctly ... everything has same RAAN
- [orbital](https://github.com/RazerM/orbital) reading tles, plotting, appears dead
- [spg4](https://github.com/brandon-rhodes/python-sgp4) propagation, seems ok
- [tle-tools](https://pypi.org/project/TLE-tools/) not sure value, seems dead
- [ESA: pykep](https://esa.github.io/pykep/index.html) more for inter-planetary stuff
- [astrodynamics](https://github.com/dinkelk/astrodynamics) looks good, but it is Matlab code
- [OrPytal](https://github.com/nicklafarge/OrPytal) does orbits without specific parameters

# References

- [Wiki: Earth parameters](https://en.wikipedia.org/wiki/Earth)
- [Wiki: Orbital elements](https://en.wikipedia.org/wiki/Orbital_elements)
- [Wiki: TLE Format](https://en.wikipedia.org/wiki/Two-line_element_set)
- [celestrak.com TLEs](https://celestrak.com/NORAD/elements/)

# MIT License

**Copyright (c) 2020 Kevin J. Walchko**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
