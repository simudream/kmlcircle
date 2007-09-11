#!/usr/bin/env python

import math
from string import Template

import sys
sys.path.append("../python")

from kmlcircle import *


def nauticalMilesToMeters(x): 
    return 1852.0 * x

def milesToMeters(x):
    return 1609.344 * x


def kml_header(docname):
    s = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.1">
  <Document>
    <name>$name</name>
    <open>1</open>
  <Style id="examplePolyStyle">
    <PolyStyle>
      <fill>1</fill>
      <outline>1</outline>
      <color>7f0000ff</color>
      <colorMode>normal</colorMode>
    </PolyStyle>
    <LineStyle>
      <color>efffffff</color>
      <colorMode>normal</colorMode>
      <width>4</width>
    </LineStyle>
  </Style>
"""
    t = Template(s)
    return t.substitute(name=docname)

def kml_footer():
    return "</Document>\n</kml>\n"

def kml_folder_start(foldername, folderdescription):
    s = """
    <Folder>
      <name>$name</name>
      <description>$description</description>
"""
    t = Template(s)
    return t.substitute(name=foldername, description=folderdescription)

def kml_folder_end():
    return "</Folder>\n"

def kml_lookat(long, lat, alt, range=0, heading=0, tilt=0):
    s = "<LookAt>\n"
    s += "<longitude>" + str(long) + "</longitude>\n"
    s += "<latitude>" + str(lat) + "</latitude>\n"
    s += "<altitude>" + str(alt) + "</altitude>\n"
    s += "<range>" + str(range) + "</range>\n"
    s += "<heading>" + str(heading) + "</heading>\n"
    s += "<tilt>" + str(tilt) + "</tilt>\n"
    s += "</LookAt>\n"
    return s

#
# Simple pushpin placemark
#
def kml_placemark_point(name, description, long, lat):
    s ="""
      <Placemark>
        <name>$nametag</name>
        <description>$desctag</description>
        <Point>
          <coordinates>$longtag, $lattag</coordinates>
        </Point>
      </Placemark>
"""
    t = Template(s)
    return t.substitute(nametag=name, desctag=description,
                        longtag=str(long), lattag=str(lat))      

def my_kml_disk(long, lat, meters, segments, name):
    s = "<Placemark>"
    s += "<styleUrl>#examplePolyStyle</styleUrl>"
    s += "<name>" + name + "</name>\n"
#    s += "<Point><coordinates>\n"
#    s += str(long) + ", " + str(lat)
#    s += "</coordinates></Point>\n";
    s += kml_regular_polygon(long, lat, meters, segments, 30)
#    s += kml_star(long, lat, meters, meters * 0.60, 20, 0.0)
    s += "</Placemark>\n";
    return s

#
#
# 12, 67% of accuracy nautical miles
#
percentile67 = [(i[0], nauticalMilesToMeters(i[1])) for i in ((12,39),(24,69),(36,99),(48,124),(72,179),(96,252),(120,326))]

#
# Current forcast of position
#
forecast = [[-73.7,31.1], [-75.5, 32.3], [-76.8, 33.5], [-76.6, 35.0], [-73.5, 37.5], [-67.5, 40.5], [-58.0,  43.0]]

circles = zip(forecast, percentile67)

print kml_header("DOCNAME")
print kml_folder_start("NAME", "DESCRIPTION")
print kml_lookat(-72.2, 30.4, 4000000)

for i in circles:
    print kml_placemark_point(str(i[1][0]) + "H", "foo",  i[0][0], i[0][1])
    print my_kml_disk(i[0][0], i[0][1], i[1][1], 25, str(i[1][0]) + "H")
print kml_folder_end()
print kml_footer()

