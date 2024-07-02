from __future__ import print_function

import os
import sys
import glob

import arcscriptsdir

import shapefile

filenames = sys.argv[1:]

def prettify(stuff, precision):
    if type(stuff)==list:
        raise Exception("stuff should not be a list")
    try:
        formatstring = "%%.%df" % precision
        return formatstring % float(stuff)
    except TypeError:
        return str(stuff)
    except ValueError:
        return str(stuff)

def structure(x, depth=-1):
    depth += 1
    prefix = " " * depth
    if not hasattr(x, "__iter__"):
        return prefix+prettify(x, 1) + "\n"
    else:
        if all([not hasattr(i, "__iter__") for i in x]):
            return prefix + ",".join([prettify(i, 1) for i in x]) + "\n"
        else:
            retval=prefix + "[\n"
            for i in x:
                retval += structure(i, depth)
            retval += prefix + "]\n"
            return retval

def _sf_getfields(filename):
    sf = shapefile.Reader(filename)
    fields = sf.fields[1:] # ignore deletion flag
    fieldnames = [x[0] for x in fields]
    return fieldnames

def makenestedlist(shape):
    points = shape.points
    if hasattr(shape,"z"):
                points = [(x,y,z) for (x,y),z in zip(points,shape.z)]
    parts = list(shape.parts) + [len(points)]
    return [points[parts[x]:parts[x+1]] for x in range(len(parts)-1)]

def ReadFeatures(filename):
    sf = shapefile.Reader(filename)
    data = sf.shapeRecords()
    fieldnames = _sf_getfields(filename)
    fid = 0
    for record in data:
        attrdict = []
        for name,value in zip(fieldnames,record.record):
            attrdict += [(str(name),prettify(value,5))] # str maintains py2 output appearance
        yield fid,makenestedlist(record.shape),attrdict
        fid += 1

for pattern in filenames:
    for filename in glob.glob(pattern+".shp"):
        print("Shapefile ",filename,"====================================")
        
        for fid,shapes,attr in ReadFeatures(filename):
            print("Item",fid)
            print(structure(shapes), end=' ')
            print(attr)

        print()
        print()
        print()
