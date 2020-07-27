#!/usr/bin/env python
# 
# Universal Wrench Holder generator
# 
# 

import solid
import solid.utils
import euclid3

######################################################################
# Users selectable parameters
######################################################################
# A list of all wrench slots, smallest to largest, and their width
slots= [0.16, 0.21, 0.23, 0.23, 0.27, 0.3]
# How wide the small end of the holder is
widthFront= 4
# How wide the back end of the holder is
widthBack= 8
# Depth of the wrench channel at the front (smallest wrench)
depthFront= 0.45
# Depth of the wrench channel at the back (largest wrench)
depthBack= 0.7
# Minimum height of the holder below bottom of the wrench channel 
# (so that the wrenches are "above ground")
# I generally measure this on the largest wrench
height= 0.4
# Width of the holding tabs
barWidth= 0.8

######################################################################

######################################################################
# Expert selectable parameters
######################################################################

# All dimensions above get multiplied by this factor.
# 25.4 = OpenSCAD units to inches
printScale= 25.4;

# This is the radius unit of the cylinder at the top of the bars
# Outside radius is set to 1.5 x cylScale (in mm)
# Inside radius is set to 0.5 x cylScale (in mm)
cylScale= 2.54 

# Maximum lengh of the "bar stock" we have to work from
# Set to 250 which exceeds what my 3D printer will print
barLen= 250;

# How thick the bars are at either end of the wrench holder
endBarScale= 1.0 * 2

######################################################################


######################################################################
# Build a pressure bar
######################################################################

frontBar= solid.utils.translate([0, 0, -cylScale * 20]) \
            (solid.cube([cylScale * endBarScale, barLen, cylScale * 21.5]))

backBar= solid.utils.translate([0, 0, -cylScale * 20]) \
            (solid.cube([cylScale * endBarScale, barLen, cylScale * 20]))

holderBarCyl= solid.utils.rotate(a=-90, v=solid.utils.RIGHT_VEC) \
           (solid.cylinder(h=barLen, r= 1.5 * cylScale, segments=48) - \
            solid.utils.down(5)(solid.cylinder(h=barLen + 10, r= 0.5 * cylScale, segments=24)))

holderBarSlicer= solid.utils.translate([-2.5 * cylScale, -5, -5 * cylScale]) \
                    ((solid.cube([5 * cylScale, barLen + 10, 5 * cylScale])))

holderBarFront= solid.utils.translate([-1.5 * cylScale, 0, -2 * cylScale]) \
                (solid.cube([cylScale, barLen, cylScale * 2]))

holderBarBack= solid.utils.translate([0.5 * cylScale, 0, -20 * cylScale]) \
                (solid.cube([cylScale, barLen, cylScale * 20]))

holderBar= holderBarFront + holderBarBack + (holderBarCyl - holderBarSlicer)


######################################################################
# Build the collection of pressure bars
######################################################################
position= 0
bars= solid.utils.translate([position, 0, 0])(frontBar)
position += cylScale * endBarScale
for i in range(0, len(slots)):
  position += (slots[i] * printScale) + (cylScale * 1.5)
  bars += solid.utils.translate([position, 0, 0])(holderBar)
  position += cylScale * 1.5
bars += solid.utils.translate([position, 0, 0])(backBar)
position += cylScale * endBarScale
barSize= position

barFront= (barLen - widthFront * printScale) / 2
barBack= (barLen - widthBack * printScale) / 2

######################################################################
# Build the extruders on the sides to cut the holder
# in a trapezoidal shape
######################################################################
extruderPath= [euclid3.Point3(0,0, -50 * cylScale), euclid3.Point3(0, 0, 2 * cylScale)]
extruderShape1= [euclid3.Point3(-0.1, -0.01, 0), \
                 euclid3.Point3(-0.1, barBack, 0), \
                 euclid3.Point3(barSize + 0.1, barFront, 0), \
                 euclid3.Point3(barSize + 0.1, -0.1, 0)]
extruder1= solid.utils.translate([barSize, 0, 0]) \
             (solid.utils.extrude_along_path(shape_pts=extruderShape1, path_pts=extruderPath))


extruderShape2= [euclid3.Point3(-0.01, barLen + 0.1, 0), \
                 euclid3.Point3(barSize + 0.01, barLen + 0.01, 0), \
                 euclid3.Point3(barSize + 0.01, barLen - barFront, 0), \
                 euclid3.Point3(-0.01, barLen - barBack, 0)]
extruder2= solid.utils.translate([barSize, 0, 0]) \
             (solid.utils.extrude_along_path(shape_pts=extruderShape2, path_pts=extruderPath))

######################################################################
# Build the base of the bars - varying so that the tops of all 
# wrenches are more or less flush with the top of the holder
######################################################################
basePath= [euclid3.Point3(0,0,0), euclid3.Point3(0, 0, -20 * cylScale)]
baseShape= [euclid3.Point3(0, 0, cylScale * 1.5 - (depthFront * printScale)), \
            euclid3.Point3(barSize, 0, cylScale * 1.5 - (depthBack * printScale)), \
            euclid3.Point3(barSize, barLen, cylScale * 1.5 - (depthBack * printScale)), \
            euclid3.Point3(0, barLen, cylScale * 1.5 - (depthFront * printScale))]
base= solid.utils.extrude_along_path(shape_pts=baseShape, path_pts=basePath)

######################################################################
# Build the "cutter" that will remove the bottom of the holder
######################################################################
bottomPath= [euclid3.Point3(0,0, cylScale * 1.5 - (depthBack + height) * printScale), euclid3.Point3(0, 0, -100 * cylScale)]
bottomShape= [euclid3.Point3(-1, -1, 0), \
              euclid3.Point3(barSize + 1, -1, 0), \
              euclid3.Point3(barSize + 1, barLen + 1, 0), \
              euclid3.Point3(-1, barLen +1, 0)]
bottom= solid.utils.extrude_along_path(shape_pts=bottomShape, path_pts=bottomPath)

######################################################################
# Extrude out a trapezoidal shape in the center of the holder so
# that each wrench is held on two tabs
######################################################################
topPath= [euclid3.Point3(0,0, cylScale * 2), euclid3.Point3(0, 0, endBarScale * 2 + cylScale * 1.5 - (depthBack + height) * printScale)]
topShape= [euclid3.Point3(-0.01, barFront + (barWidth * printScale), 0), \
           euclid3.Point3(barSize + 0.01, barBack + (barWidth * printScale), 0), \
           euclid3.Point3(barSize + 0.01, barLen - barBack - (barWidth * printScale), 0), \
           euclid3.Point3(-0.01, barLen - barFront - (barWidth * printScale), 0)]
top= solid.utils.extrude_along_path(shape_pts=topShape, path_pts=topPath)

######################################################################
# Final construction
######################################################################
holder = bars + base
holder = holder - extruder1
holder = holder - extruder2
holder = holder - bottom
holder = holder - top


######################################################################
# And print it out
######################################################################
print(solid.scad_render(holder))


