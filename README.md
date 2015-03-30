# kmlcircle
Automatically exported from code.google.com/p/kmlcircle

$ ./kmlcircle.py   
help


-h, --longitude longitude in degrees (h is for 'horizontal')
-v, --latitude  latitude in degrees (v is for 'vertical')
-r, --radius    radius in meters
-s, --sides     number of sides
-i, --inner     optional, inner radius in meters,  default same as 'radius'
                this will make a 'star'
-o, --offset    optional, rotate polygon by angle in degrees, default 0

to make a square, -s == 4
to make a circle, -s > 20
./kmlcircle.py -h -81.0 -v 14.2 -s 4 -r 10000

<textarea name="myTextArea" cols="100" rows="20" readonly=readonly>
<Polygon>
  <outerBoundaryIs><LinearRing><coordinates>
    -80.9073366544,14.2
    -81.0000183885,14.2898320472
    -81.0926633311,14.1999643609
    -80.9999816261,14.1101679528
    -80.9073366544,14.2
  </coordinates></LinearRing></outerBoundaryIs>
</Polygon>
</textarea>

to make a star, use -i (in meters)
./kmlcircle.py -h -81.0 -v 14.2 -s 5 -r 10000 -i 8000

<textarea name="myTextArea" cols="100" rows="20" readonly=readonly>
<Polygon>
  <outerBoundaryIs><LinearRing><coordinates>
    -80.9073366544,14.2
    -80.9400227376,14.2422433176
    -80.9713721103,14.2854391569
    -81.0229257573,14.2683436674
    -81.0749945256,14.2527758529
    -81.074130669,14.199977191
    -81.0749379541,14.1471719883
    -81.0228895515,14.1316471062
    -80.9713587556,14.114568453
    -80.9400312846,14.1577602066
    -80.9073366544,14.2
    -80.9400227376,14.2422433176
  </coordinates></LinearRing></outerBoundaryIs>
</Polygon>
</textarea>
