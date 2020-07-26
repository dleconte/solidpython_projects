#!/usr/bin/env python

import solid
import solid.utils
import euclid3

printScale= 25.4;


cylScale= 1.0
barLen= 250;

endBarScale= 1.5

slots= [0.16, 0.21, 0.23, 0.23, 0.27, 0.3]
widthFront= 4
widthBack= 8
depthFront= 0.45
depthBack= 0.7
height= 0.4
barWidth= 0.8


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


position= 0
bars= solid.utils.translate([position, 0, 0])(frontBar)
position += cylScale * endBarScale
for i in range(0, len(slots)):
  position += (slots[i] * printScale) + (cylScale * 1.5)
  bars += solid.utils.translate([position, 0, 0])(holderBar)
  position += cylScale * 1.5
bars += solid.utils.translate([position, 0, 0])(backBar)
position += cylScale * 1.5
barSize= position

barFront= (barLen - widthFront * printScale) / 2
barBack= (barLen - widthBack * printScale) / 2

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

basePath= [euclid3.Point3(0,0,0), euclid3.Point3(0, 0, -20 * cylScale)]
baseShape= [euclid3.Point3(0, 0, cylScale * 1.5 - (depthFront * printScale)), \
            euclid3.Point3(barSize, 0, cylScale * 1.5 - (depthBack * printScale)), \
            euclid3.Point3(barSize, barLen, cylScale * 1.5 - (depthBack * printScale)), \
            euclid3.Point3(0, barLen, cylScale * 1.5 - (depthFront * printScale))]
base= solid.utils.extrude_along_path(shape_pts=baseShape, path_pts=basePath)

bottomPath= [euclid3.Point3(0,0, cylScale * 1.5 - (depthBack + height) * printScale), euclid3.Point3(0, 0, -100 * cylScale)]
bottomShape= [euclid3.Point3(-1, -1, 0), \
              euclid3.Point3(barSize + 1, -1, 0), \
              euclid3.Point3(barSize + 1, barLen + 1, 0), \
              euclid3.Point3(-1, barLen +1, 0)]
bottom= solid.utils.extrude_along_path(shape_pts=bottomShape, path_pts=bottomPath)

topPath= [euclid3.Point3(0,0, cylScale * 2), euclid3.Point3(0, 0, 1 + cylScale * 1.5 - (depthBack + height) * printScale)]
topShape= [euclid3.Point3(-0.01, barFront + (barWidth * printScale), 0), \
           euclid3.Point3(barSize + 0.01, barBack + (barWidth * printScale), 0), \
           euclid3.Point3(barSize + 0.01, barLen - barBack - (barWidth * printScale), 0), \
           euclid3.Point3(-0.01, barLen - barFront - (barWidth * printScale), 0)]
top= solid.utils.extrude_along_path(shape_pts=topShape, path_pts=topPath)

holder = bars + base
holder = holder - extruder1
holder = holder - extruder2
holder = holder - bottom
holder = holder - top

#print(solid.scad_render(top))
#print(solid.scad_render(solid.utils.translate([100,0,0])(ex1)))

print(solid.scad_render(holder))




#print(solid.scad_render(a))
#print(solid.scad_render(b))
#print(solid.scad_render(d))
