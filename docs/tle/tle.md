# TLE

![](../pics/tle.gif)

- [celestrak.com: TLE format](https://www.celestrak.com/NORAD/documentation/tle-fmt.php)


The file extension ".tle" commonly designates a list of elements of orbiting satellites in
the two-line format of NORAD.

The positions and velocities of satellites are updated periodically by NORAD, and provided
to  users  through their bulletin boards and anonymous ftp sites.  A variety of models may
be applied to these element sets in order to predict the future position and velocity of a
particular  satellite.   However,  it  is important to note that the NORAD output data are
mean values, i.e., periodic perturbations have been removed.  Thus, any  predictive  model
must  be  compatible  with  the  NORAD  models,  in  the sense that the same terms must be
canceled.  There are several models which accomplish this goal.

Data for each satellite consists of three lines in the following format:

000000000111111111122222222223333333333444444444455555555556666666666
123456789012345678901234567890123456789012345678901234567890123456789

AAAAAAAAAAAAAAAAAAAAAA
These lines are encoded as follows:

LINE 0
A line containing a single 22-character ASCII string giving the name of the satellite.

LINE 1
Column Description

01-01  Line Number of Element Data, in this case, 1.

03-07  Satellite Number.  Each time a satellite is launched NORAD assigns a number to that
       satellite.   Vanguard  1  is the earliest satellite whose elements can currently be
       found (all earlier birds must have reentered by now). It was  launched  on  3/17/58
       and carries "00005" as a NORAD Catalog number.

10-11  International  Designator--the  last  two  digits  of  the  year  the satellite was
       launched.  This number is for reference only and is not used by  tracking  programs
       for predictions. Thus it may be omitted in some element sets.

12-14  International Designator--the number of the launch for that year.  This number does
       not give any indication as to when during the  year  the  bird  went  up  just  its
       ranking  among its fellow launches for that year. This number is for reference only
       and is not used by tracking programs for predictions. Thus it  may  be  omitted  in
       some element sets.

15-17  International  Designator--piece  of  launch.  On many launches there are more than
       one payload.  This number is for  reference  only  and  is  not  used  by  tracking
       programs for predictions. Thus it may be omitted in some element sets.

19-20  Epoch Year--The last two digits of the year when the element set was measured.

21-32  Epoch  Day--The  Julian  Day and fractional portion of the day when the element set
       was measured.

34-43  First Time Derivative of the Mean Motion or Ballistic  Coefficient--  depending  on
       ephemeris type.

45-52  Second Time Derivative of Mean Motion (decimal point assumed; blank if N/A)

54-61  BSTAR  drag term if GP4 general perturbation theory was used.  Otherwise, radiation
       pressure coefficient.  (Decimal point assumed.)   This  number  usually  refers  to
       atmospheric drag on a satellite. However, at times satellites are strongly affected
       by the gravitational pull of bodies other than the Earth (ie: Sun and Moon).  While
       it  seems  unlikely,  drag  can  actually  be  a negative number thus indicating an
       increase in orbital energy rather than a decrease. This happens when  the  Sun  and
       Moon  combine  to  pull the satellite's apogee to a higher altitude.  However, this
       condition of negative drag is only valid for as long as the gravitational situation
       warrants  it.  So,  some  folks like to zero out negative drag factors for smoother
       orbital calculations.

63-63  Ephemeris type.  This code indicates the type of model used to generate the element
       set.  Allowed values and their corresponding models are:

           1 = SGP
           2 = SGP4
           3 = SDP4
           4 = SGP8
           5 = SDP8

       The  models  designated  "SG*" are used for near-earth satellites (i.e., those with
       periods less than 225 minutes), and the models designated "SD*" are used for  deep-
       space  satellites  (those  with  periods  equal  to  or  greater than 225 minutes).
       Atmospheric drag is more important for near-earth satellites, while  tidal  effects
       from the sun and moon are more important for the deep-space satellites.

65-68  Element  number  (modulo 1000).  Each time a satellite's orbit is determined and an
       element set created the element set is assigned a number.

69-69  Checksum (Modulo 10).  Letters, blanks, periods, plus signs = 0;  minus  signs  =1.
       The  last  number  in  each  of  the 2 lines of an element set is a checksum.  This
       number is calculated by assigning the following values to  each  character  on  the
       line. A number carries it's own value, a minus (-) sign carries a value of one (1),
       and letters, blanks and periods (decimal points (.)) carry a value of zero (0).

LINE 2
01-01  Line Number of Element Data, in this case, 2.

03-07  Satellite Number.

09-16  Inclination (in degrees), i.e., the angle formed by the orbit to the  equator.  The
       inclination must be a positive number of degrees between 0 and 180. A zero angle of
       inclination indicates a satellite moving  from  west  to  east  directly  over  the
       equator.  An  inclination of 28 degrees (most shuttle launches) would form an angle
       of 28 degrees between the equator and  the  orbit  of  the  satellite.  Also,  that
       satellite  will  travel  only  as far north and south as +- 28 degrees latitude. On
       it's ascending orbital crossing (moving from south to north) of  the  equator,  the
       satellite  will be moving from southwest to northeast. An inclination of 90 degrees
       would mean that the satellite is moving directly from south to north and will cross
       directly  over the north and south poles. Any satellite with an inclination greater
       than 90 degrees is said to be in retrograde orbit.  This  means  the  satellite  is
       moving  in  a  direction  opposite  the  rotation of the earth. A satellite with an
       inclination of 152 degrees will be moving from southeast to northwest as  it  cross
       the  equator  from south to north. This is opposite the rotation of the Earth. This
       satellite will move as far north and south of the equator as  28  degrees  latitude
       and  be in an orbital direction exactly opposite a satellite with an inclination of
       28 degrees.

18-25  Right ascension of ascending node (RAAN or RA  of  Node).   In  order  to  fix  the
       position  of  an  orbit  in  space  it is necessary to refer to a coordinate system
       outside the earth  coordinate  system.  Because  the  Earth  rotates  latitude  and
       longitude  coordinates do not indicate an absolute frame of reference. Therefore it
       was decided to use astronomical conventions to fix orbits relative to the celestial
       sphere  which  is  delineated  in degrees of Right Ascension and declination. Right
       ascension is similar to longitude and Declination is similar to latitude.  When  an
       element  set  is  taken  Right  Ascension  of the ascending Node is computed in the
       following manner. As a satellite moves about the center of the earth it crosses the
       equator  twice.  It  is  either  in  ascending  node, moving from south to north or
       descending node moving from north to south. The RAAN is taken  from  the  point  at
       which  the  orbit  crosses  the  equator moving from south to north. If you were to
       stand at the center of the planet and look  directly  at  the  location  where  the
       satellite  crossed the equator you would be pointing to the ascending node. To give
       this line a value the angle is measured between  this  line  and  0  degrees  right
       ascension  (RA). Again standing at the center of the earth 0 degrees RA will always
       point to the same location on the celestial sphere.

27-33  Eccentricity.  In general, satellites execute elliptical orbits  about  the  Earth.
       The  center  of  the  ellipse  is  at  one  of  the  two  foci of the ellipse.  The
       eccentricity of the orbit is the ratio of the distance  between  the  foci  to  the
       major axis of the ellipse, i.e., the longest line between any two points.  Thus the
       ellipticity is 0 for a perfectly circular orbit and approaches 1.0 for orbits which
       are highly elongated.

35-42  Argument  of  Perigee  (degrees).   The  orbital  position corresponding to closest
       approach of a satellite to the Earth is called perigee.  The argument of perigee is
       the  angle measured from the center of the Earth between the ascending node and the
       perigee along the plane of the orbit (inclination). If the Argument of  perigee  is
       zero  (0) then the lowest point of the orbit of that satellite would be at the same
       location as the point where it crossed the equator in it's ascending node.  If  the
       argument  of  perigee  is  180  then  the lowest point of the orbit would be on the
       equator on the opposite side of the earth from the ascending node.

44-51  Mean Anomaly (degrees).  The mean anomaly fixes the position of  the  satellite  in
       the  orbit  as  described  above.  So  far  we have only talked about the shape and
       location of the orbit of the satellite. We haven't placed the satellite along  that
       path and given it an exact location. That's what Mean Anomaly does. Mean Anomaly is
       measured from the point of perigee. In the Argument of perigee example above it was
       stated  that  an Arg of Perigee of zero would place perigee at the same location as
       the Ascending node. If in this case the MA were  also  zero  then  the  satellite's
       position  as  of the taking of the element set would also located directly over the
       equator at the ascending node. If the Arg of Perigee was 0 degrees and the  MA  was
       180  degrees then the satellite's position would have been on the other side of the
       earth just over the equator as it was headed from north to south.

53-63  Mean Motion (revolutions per day).  The mean motion of a satellite  is  simply  the
       number  of orbits the satellite makes in one solar day (regular day, common day, 24
       hours, 1440 minutes, 86400 seconds etc.). This number also generally indicates  the
       orbit altitude.

64-68  Revolution number at epoch (revs).  Theoretically, this number equals the number of
       orbits the satellite  has  completed  since  it's  launch,  modulo  100,000.   Some
       satellites  have  incorrect  epoch  orbit  numbers.   Oscar 10 is just such a case.
       However,  this  number  is  provided  more  for  reference  purposes  than  orbital
       calculation.  And so, its accuracy or lack thereof doesn't affect the accuracy of a
       prediction.

69-69  Check Sum (modulo 10).  As with Line 1,  this  number  is  provided  to  check  the
       accuracy of the element set. It's calculation is described above.

# References

- [celestrak.com tle format](https://celestrak.com/NORAD/documentation/tle-fmt.php)
- [Ubuntu man pages for tle](https://manpages.ubuntu.com/manpages/precise/man5/tle.5.html)
