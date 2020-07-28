#!/usr/bin/env python
# 
# Universal Wrench Holder generator
# 
# 

import solid
import solid.utils
import euclid3

'''
######################################################################
# Users selectable parameters (Proto)
######################################################################
# A list of all wrench slots, smallest to largest, and their width
slots= [0.16, 0.21, 0.23, 0.23, 0.27, 0.3]
# How wide the small end of the holder is
widthFront= 4
widthFrontLeft= 0
widthFrontRight= 0
# How wide the back end of the holder is
widthBack= 8
widthBackLeft= 0
widthBackRight= 0
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

# This is the radius unit of the cylinder at the top of the bars
# Outside radius is set to 1.5 x cylScale (in mm)
# Inside radius is set to 0.5 x cylScale (in mm)
cylScale= 2.54

# Maximum lengh of the "bar stock" we have to work from
# Set to 250 which exceeds what my 3D printer will print
barLen= 250;

# How thick the bars are at either end of the wrench holder
endBarScale= 1.0 * 2
'''

'''
######################################################################
# Users selectable parameters (Pittsburgh large)
######################################################################
# A list of all wrench slots, smallest to largest, and their width
slots= [0.245, 0.255, 0.27, 0.33, 0.335]
# How wide the small end of the holder is
widthFront= 7.25
widthFrontLeft= 0
widthFrontRight= 0
# How wide the back end of the holder is
widthBack= 8.5
widthBackLeft= 0
widthBackRight= 0
# Depth of the wrench channel at the front (smallest wrench)
depthFront= 0.75
# Depth of the wrench channel at the back (largest wrench)
depthBack= 1.0
# Minimum height of the holder below bottom of the wrench channel 
# (so that the wrenches are "above ground")
# I generally measure this on the largest wrench
height= 0.85
# Width of the holding tabs
barWidth= 2.0

# This is the radius unit of the cylinder at the top of the bars
# Outside radius is set to 1.5 x cylScale (in mm)
# Inside radius is set to 0.5 x cylScale (in mm)
cylScale= 2.54

# Maximum lengh of the "bar stock" we have to work from
# Set to 250 which exceeds what my 3D printer will print
barLen= 250;

# How thick the bars are at either end of the wrench holder
endBarScale= 1.0 * 2
'''

'''
######################################################################
# Users selectable parameters (Pittsburgh small)
######################################################################
# A list of all wrench slots, smallest to largest, and their width
slots= [0.155, 0.157, 0.165, 0.165, 0.17, 0.2, 0.23, 0.23, 0.23]
# How wide the small end of the holder is
widthFront= 2.75
widthFrontLeft= 0
widthFrontRight= 0
# How wide the back end of the holder is
widthBack= 6.0
widthBackLeft= 0
widthBackRight= 0
# Depth of the wrench channel at the front (smallest wrench)
depthFront= .45
# Depth of the wrench channel at the back (largest wrench)
depthBack= .75
# Minimum height of the holder below bottom of the wrench channel 
# (so that the wrenches are "above ground")
# I generally measure this on the largest wrench
height= 0.65
# Width of the holding tabs
barWidth= 1.0

# This is the radius unit of the cylinder at the top of the bars
# Outside radius is set to 1.5 x cylScale (in mm)
# Inside radius is set to 0.5 x cylScale (in mm)
cylScale= 2.54 * 0.8

# Maximum lengh of the "bar stock" we have to work from
# Set to 250 which exceeds what my 3D printer will print
barLen= 250;

# How thick the bars are at either end of the wrench holder
endBarScale= 1.0 * 2
'''

'''
######################################################################
# Users selectable parameters (Duro Chrome)
######################################################################
# A list of all wrench slots, smallest to largest, and their width
slots= [.106, .123, .135, .155, .16, .16, .185, .185, .2, .23]
# How wide the small end of the holder is
widthFront= 1.7
widthFrontLeft= 0
widthFrontRight= 0
# How wide the back end of the holder is
widthBack= 4.7
widthBackLeft= 0
widthBackRight= 0
# Depth of the wrench channel at the front (smallest wrench)
depthFront= .35
# Depth of the wrench channel at the back (largest wrench)
depthBack= .75
# Minimum height of the holder below bottom of the wrench channel 
# (so that the wrenches are "above ground")
# I generally measure this on the largest wrench
height= 0.56
# Width of the holding tabs
barWidth= 0.8

# This is the radius unit of the cylinder at the top of the bars
# Outside radius is set to 1.5 x cylScale (in mm)
# Inside radius is set to 0.5 x cylScale (in mm)
cylScale= 2.54 * 0.8

# Maximum lengh of the "bar stock" we have to work from
# Set to 250 which exceeds what my 3D printer will print
barLen= 250;

# How thick the bars are at either end of the wrench holder
endBarScale= 1.0 * 2
'''

######################################################################
# Users selectable parameters (Chrome Vanadium Box)
######################################################################
# A list of all wrench slots, smallest to largest, and their width
slots= [.156, .16, .19, .24, .24, .27, .305, .35]
labelsLeft= ['1', "7/8", "25/32", "11/16", "9/16", "7/16", "3/8", "5/16"]
labelsLeft= ["5/16", "3/8", "7/16",  "9/16", "11/16", "25/32", "7/8", '1']
labelsRight= ["1/4", "5/16", "3/8", "1/2", "5/8", "3/4", "13/16", "15/16"]
# How wide the small end of the holder is
widthFront= 0
widthFrontLeft= 2.7 / 2.
widthFrontRight= 2.7 / 2.
# How wide the back end of the holder is
widthBack= 0
widthBackLeft= 2.7 / 2.
widthBackRight= 5.5 - 2.7 / 2.
# Depth of the wrench channel at the front (smallest wrench)
depthFront= .35
# Depth of the wrench channel at the back (largest wrench)
depthBack= .68
# Minimum height of the holder below bottom of the wrench channel 
# (so that the wrenches are "above ground")
# I generally measure this on the largest wrench
height= 0.45
# Width of the holding tabs
barWidth= 1.0

# This is the radius unit of the cylinder at the top of the bars
# Outside radius is set to 1.5 x cylScale (in mm)
# Inside radius is set to 0.5 x cylScale (in mm)
cylScale= 2.54 * 1.0

# Maximum lengh of the "bar stock" we have to work from
# Set to 250 which exceeds what my 3D printer will print
barLen= 250;

# How thick the bars are at either end of the wrench holder
endBarScale= 1.0 * 2

######################################################################

######################################################################
# Expert selectable parameters
######################################################################

# All dimensions above get multiplied by this factor.
# 25.4 = OpenSCAD units to inches
printScale= 25.4;


######################################################################


######################################################################
# Build a pressure bar
######################################################################

#frontBar= solid.utils.translate([0, 0, -cylScale * 20]) \
#            (solid.cube([cylScale * endBarScale, barLen, cylScale * 20]))

frontBar= solid.utils.translate([endBarScale * cylScale / 2, 0, (3 - endBarScale) * cylScale / 2.0]) \
            (solid.utils.rotate(a=-90, v=solid.utils.RIGHT_VEC) \
            (solid.cylinder(h=barLen, r= endBarScale * cylScale / 2, segments=48))) \
          + \
          solid.utils.translate([0, 0, -cylScale * 20]) \
            (solid.cube([cylScale * endBarScale, barLen, cylScale * 21.5 - (endBarScale  * cylScale / 2)]))

backBar= solid.utils.translate([endBarScale * cylScale / 2, 0, (3 - endBarScale) * cylScale / 2.0]) \
            (solid.utils.rotate(a=-90, v=solid.utils.RIGHT_VEC) \
            (solid.cylinder(h=barLen, r= endBarScale * cylScale / 2, segments=48))) \
          + \
          solid.utils.translate([0, 0, -cylScale * 20]) \
            (solid.cube([cylScale * endBarScale, barLen, cylScale * 21.5 - (endBarScale  * cylScale / 2)])) \
          + \
          solid.utils.translate([-cylScale * 1.5 , 0, cylScale * 0.5]) \
            (solid.cube([cylScale * (3 + endBarScale) / 2, barLen, cylScale]))

#backBar= solid.utils.translate([0, 0, -cylScale * 20]) \
#            (solid.cube([cylScale * endBarScale, barLen, cylScale * 20]))

holderBarCyl= solid.utils.rotate(a=-90, v=solid.utils.RIGHT_VEC) \
           (solid.cylinder(h=barLen, r= 1.5 * cylScale, segments=48) - \
            solid.utils.down(5)(solid.cylinder(h=barLen + 10, r= 0.5 * cylScale, segments=24)))

holderBarSlicer= solid.utils.translate([-2.5 * cylScale, -5, -5 * cylScale]) \
                    ((solid.cube([5 * cylScale, barLen + 10, 5 * cylScale])))

holderBarFront= solid.utils.translate([-1.5 * cylScale, 0, -4 * cylScale]) \
                (solid.cube([cylScale, barLen, cylScale * 4]))

holderBarBack= solid.utils.translate([0.5 * cylScale, 0, -20 * cylScale]) \
                (solid.cube([cylScale, barLen, cylScale * 20]))

holderBar= holderBarFront + holderBarBack + (holderBarCyl - holderBarSlicer)


######################################################################
# Build the collection of pressure bars
######################################################################
position= 0
barPositionsX= []
bars= solid.utils.translate([position, 0, 0])(frontBar)
position += cylScale * endBarScale
barPositionsX.append(position - (cylScale * endBarScale / 2))
for i in range(0, len(slots)):
  position += (slots[i] * printScale) + (cylScale * 1.5)
  barPositionsX.append(position)
  bars += solid.utils.translate([position, 0, 0])(holderBar)
  position += cylScale * 1.5
bars += solid.utils.translate([position, 0, 0])(backBar)
position += cylScale * endBarScale
barSize= position


######################################################################
# Prepare the cutters for the bars on the side.
######################################################################
if (widthFrontLeft == 0) and (widthFrontRight) == 0:
  widthFrontLeft= widthFront / 2.0
  widthFrontRight= widthFront / 2.0
if (widthBackLeft == 0) and (widthBackRight) == 0:
  widthBackLeft= widthBack / 2.0
  widthBackRight= widthBack / 2.0
barFrontLeft= (barLen / 2.0 - widthFrontLeft * printScale)
barFrontRight= (barLen / 2.0 - widthFrontRight * printScale)
barBackLeft= (barLen / 2.0 - widthBackLeft * printScale)
barBackRight= (barLen / 2.0 - widthBackRight * printScale)
#barFront= (barLen - widthFront * printScale) / 2
#barBack= (barLen - widthBack * printScale) / 2

######################################################################
# While we are at it we can also prepare the YPositions of the 
# Labels
######################################################################
barFrontLeft= (barLen / 2.0 - widthFrontLeft * printScale)
barFrontRight= (barLen / 2.0 - widthFrontRight * printScale)
barBackLeft= (barLen / 2.0 - widthBackLeft * printScale)
barBackRight= (barLen / 2.0 - widthBackRight * printScale)
#barFront= (barLen - widthFront * printScale) / 2
#barBack= (barLen - widthBack * printScale) / 2
barPositionsYLeft= []
barPositionsYRight= []
for i in range(0, len(barPositionsX)):
  barPositionsYLeft.append(barFrontLeft + \
                           (barPositionsX[i] / barSize) * (barBackLeft - barFrontLeft))
  barPositionsYRight.append(barFrontRight + \
                           (barPositionsX[i] / barSize) * (barBackRight - barFrontRight))


######################################################################
# Build the extruders on the sides to cut the holder
# in a trapezoidal shape
######################################################################
extruderPath= [euclid3.Point3(0,0, -50 * cylScale), euclid3.Point3(0, 0, 2 * cylScale)]
#extruderShape1= [euclid3.Point3(-0.1, -0.01, 0), \
#                 euclid3.Point3(-0.1, barBack, 0), \
#                 euclid3.Point3(barSize + 0.1, barFront, 0), \
#                 euclid3.Point3(barSize + 0.1, -0.1, 0)]
extruderShape1= [euclid3.Point3(-0.1, -0.01, 0), \
                 euclid3.Point3(-0.1, barBackRight, 0), \
                 euclid3.Point3(barSize + 0.1, barFrontRight, 0), \
                 euclid3.Point3(barSize + 0.1, -0.1, 0)]
extruder1= solid.utils.translate([barSize, 0, 0]) \
             (solid.utils.extrude_along_path(shape_pts=extruderShape1, path_pts=extruderPath))


#extruderShape2= [euclid3.Point3(-0.01, barLen + 0.1, 0), \
#                 euclid3.Point3(barSize + 0.01, barLen + 0.01, 0), \
#                 euclid3.Point3(barSize + 0.01, barLen - barFront, 0), \
#                 euclid3.Point3(-0.01, barLen - barBack, 0)]
extruderShape2= [euclid3.Point3(-0.01, barLen + 0.1, 0), \
                 euclid3.Point3(barSize + 0.01, barLen + 0.01, 0), \
                 euclid3.Point3(barSize + 0.01, barLen - barFrontLeft, 0), \
                 euclid3.Point3(-0.01, barLen - barBackLeft, 0)]
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
#topShape= [euclid3.Point3(-0.01, barFront + (barWidth * printScale), 0), \
#           euclid3.Point3(barSize + 0.01, barBack + (barWidth * printScale), 0), \
#           euclid3.Point3(barSize + 0.01, barLen - barBack - (barWidth * printScale), 0), \
#           euclid3.Point3(-0.01, barLen - barFront - (barWidth * printScale), 0)]
topShape= [euclid3.Point3(-0.01, barFrontRight + (barWidth * printScale), 0), \
           euclid3.Point3(barSize + 0.01, barBackRight + (barWidth * printScale), 0), \
           euclid3.Point3(barSize + 0.01, barLen - barBackLeft - (barWidth * printScale), 0), \
           euclid3.Point3(-0.01, barLen - barFrontLeft - (barWidth * printScale), 0)]
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

######################################################################
# Then add the labels.
######################################################################
for i in range(0, len(labelsLeft)):
  if labelsLeft[i]:
    if labelsLeft[i] != "":
      a= solid.utils.translate([barPositionsX[i + 1] - cylScale * 0.15, barLen - barPositionsYLeft[i + 1] - 12, 0]) \
       (solid.utils.translate([0, 0, cylScale * 0.5]) \
       (solid.utils.rotate(-90) \
       (solid.utils.linear_extrude(height=cylScale * 1.3) \
       (solid.text(labelsLeft[i], size = cylScale * 2, font = "Roboto:style=Bold", halign = "center", valign = "center", segments=48)))))
      print(solid.scad_render(a))      
for i in range(0, len(labelsRight)):
  if labelsRight[i]:
    if labelsRight[i] != "":
      a= solid.utils.translate([barPositionsX[i + 1] - cylScale * 0.15, barPositionsYRight[i + 1] + barWidth * printScale - 12, 0]) \
       (solid.utils.translate([0, 0, cylScale * 0.5]) \
       (solid.utils.rotate(-90) \
       (solid.utils.linear_extrude(height=cylScale * 1.3) \
       (solid.text(labelsRight[i], size = cylScale * 2, font = "Roboto:style=Bold", halign = "center", valign = "center", segments=48)))))
      print(solid.scad_render(a))      

