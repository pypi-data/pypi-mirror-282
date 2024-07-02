import arcpy
import sys

def get_points(shape):
    # read geometry
    pointlist = []
    if(shape.partCount != 1):
        arcpy.AddError("Error: polyline %d has multiple parts"%arcid)
        raise Exception("Invalid polyline")
    for point in shape.getPart(0):
        pointlist.append((point.X,point.Y))
    return pointlist

fc1 = arcpy.GetParameterAsText(0)
fc2 = arcpy.GetParameterAsText(1)

def readrows(fc):
    rows = arcpy.SearchCursor(fc)
    shapefieldname = arcpy.Describe(fc).ShapeFieldName
    fields = [f.name for f in arcpy.ListFields(fc) if f.name!=shapefieldname]
    shapes = []
    data = []
    for row in rows:
        shape = row.getValue(shapefieldname)
        shapes += [get_points(shape)]
        rowdata = {}
        for name in fields:
            rowdata[name] = row.getValue(name)
        data += [rowdata]
    del row
    del rows
    return fields,shapes,data

names1,shapes1,data1 = readrows(fc1)
names2,shapes2,data2 = readrows(fc2)

if not names1==names2:
    arcpy.AddWarning("Fields do not match")
    sys.exit()

if not len(shapes1)==len(shapes2):
    arcpy.AddWarning("length does not match")
    sys.exit()

for num,(shape1,shape2) in enumerate(zip(shapes1,shapes2)):
    if not shape1==shape2:
        arcpy.AddWarning("Shape of item %d does not match"%num)

for num,(d1,d2) in enumerate(zip(data1,data2)):
    for name in names1:
        if not d1[name]==d2[name]:
            arcpy.AddWarning("Fields differ: field %s, item %d"%(name,num))
