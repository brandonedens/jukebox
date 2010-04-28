#!BPY
"""
Name: 'inkscape export (.svg)'
Blender: 244
Group: 'Export'
Tooltip: 'Export selected mesh to inkscape Format (.svg)'
"""

__author__ = 'Brandon Edens'
__url__ = ("blender", "blenderartists.org")
__version__ = "1.1"

__bpydoc__ = """\
        This script exports the selected mesh to inkscape (www.inkscape.org) file format (i.e.: .svg)

        The starting point of this script was Anthony D'Agostino's raw triangle format export.
        (some code is still here and there, cut'n pasted from his script)

        Usage:<br>
            Select the mesh to be exported and run this script from "File->Export" menu.
            The toggle button 'export 3 files' enables the generation of 4 files: one global
            and three with the three different views of the object.
            This script is licensed under the GPL license. (c) Dino Ghilardi, 2005

"""

# .svg export, mostly brutally cut-n pasted from the
# 'Raw triangle export' (Anthony D'Agostino, http://www.redrival.com/scorpius)|

import Blender
from Blender import Draw
import BPyObject
#, meshtools
import sys
import bpy
#import time
import math

OFFSET=1e-5

# =================================
# === Write inkscape Format.===
# =================================

def collect_edges(edges):
    """Gets the max-min coordinates of the mesh"""

    """Getting the extremes of the mesh to be exported"""

    maxX=maxY=maxZ = -1000000000
    minX=minY=minZ =  1000000000

    FGON= Blender.Mesh.EdgeFlags.FGON

    me = bpy.data.meshes.new()
    for ob_base in bpy.data.scenes.active.objects.context:
        for ob in BPyObject.getDerivedObjects(ob_base):
            me.verts = None
            try:    me.getFromObject(ob[0])
            except: pass

            if me.edges:
                me.transform(ob[1])

                for ed in me.edges:
                    if not ed.flag & FGON:
                        x,y,z = v1 = tuple(ed.v1.co)
                        maxX = max(maxX, x)
                        maxY = max(maxY, y)
                        maxZ = max(maxZ, z)
                        minX = min(minX, x)
                        minY = min(minY, y)
                        minZ = min(minZ, z)

                        x,y,z = v2 = tuple(ed.v2.co)
                        maxX = max(maxX, x)
                        maxY = max(maxY, y)
                        maxZ = max(maxZ, z)
                        minX = min(minX, x)
                        minY = min(minY, y)
                        minZ = min(minZ, z)

                        edges.append( (v1, v2) )

    me.verts = None # free memory
    return maxX,maxY,maxZ,minX,minY,minZ

def inkscapefooter(file):
    file.write('</svg>\n')

def inkscapeheader(file):
    file.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
    file.write('<!-- Created with Inkscape (http://www.inkscape.org/) -->\n')
    file.write('<svg\n')
    file.write('xmlns:dc="http://purl.org/dc/elements/1.1/"\n')
    file.write('xmlns:cc="http://creativecommons.org/ns#"\n')
    file.write('xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"\n')
    file.write('xmlns:svg="http://www.w3.org/2000/svg"\n')
    file.write('xmlns="http://www.w3.org/2000/svg"\n')
    file.write('xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"\n')
    file.write('xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"\n')

    file.write('version="1.0"\n')
    file.write('width="2160"\n')
    file.write('height="1080"\n')
    file.write('id="svg2">\n')

    file.write('<sodipodi:namedview\n')
    file.write('inkscape:document-units="in"\n')
    file.write('pagecolor="#ffffff"\n')
    file.write('bordercolor="#666666"\n')
    file.write('borderopacity="1.0"\n')
    file.write('inkscape:pageopacity="0.0"\n')
    file.write('inkscape:pageshadow="2"\n')
    file.write('inkscape:zoom="0.73425926"\n')
    file.write('inkscape:cx="1080"\n')
    file.write('inkscape:cy="540"\n')
    file.write('inkscape:current-layer="layer1"\n')
    file.write('id="namedview2387"\n')
    file.write('showgrid="true"\n')
    file.write('units="in"\n')
    file.write('inkscape:window-width="1678"\n')
    file.write('inkscape:window-height="1029"\n')
    file.write('inkscape:window-x="0"\n')
    file.write('inkscape:window-y="19"\n')
    file.write('showguides="true"\n')
    file.write('inkscape:guide-bbox="true"\n')
    file.write('inkscape:snap-global="true"\n')
    file.write('objecttolerance="1"\n')
    file.write('gridtolerance="10"\n')
    file.write('guidetolerance="15">\n')
    file.write('<inkscape:grid\n')
    file.write('type="xygrid"\n')
    file.write('id="grid2379"\n')
    file.write('units="in"\n')
    file.write('visible="true"\n')
    file.write('enabled="true"\n')
    file.write('spacingx="0.125in"\n')
    file.write('spacingy="0.125in"\n')
    file.write('empspacing="4" />\n')
    file.write('</sodipodi:namedview>\n')

def figdata(file, edges, expview, bounds, scale, space):
    maxX,maxY,maxZ,minX,minY,minZ = bounds

    def point(edge):
        return edge[0] == edge[2] and edge[1] == edge[3]

    def same_edge(edge1, edge2):
        equal = edge1[0] == edge2[0] and edge1[1] == edge2[1] and edge1[2] == edge2[2] and edge1[3] == edge2[3]
        opposite = edge1[0] == edge2[2] and edge1[1] == edge2[3] and edge1[2] == edge2[0] and edge1[3] == edge2[1]
        return equal or opposite

    def normalize(edge):
        if edge[2] < edge[0] or (edge[0] == edge[2] and edge[3] < edge[1]):
            return (edge[2], edge[3], edge[0], edge[1])
        else:
            return edge

    def xytransform(ed):
        """gives the face vertexes coordinates in the inkscape format/translation (view xy)"""
        x1,y1,z1 = ed[0]
        x2,y2,z2 = ed[1]
        y1=-y1; y2=-y2
        return x1,y1,z1,x2,y2,z2

    def xztransform(ed):
        """gives the face vertexes coordinates in the inkscape format/translation (view xz)"""
        x1,y1,z1 = ed[0]
        x2,y2,z2 = ed[1]
        y1=-y1
        y2=-y2

        z1=-z1+maxZ-minY +space
        z2=-z2+maxZ-minY +space
        return x1,y1,z1,x2,y2,z2

    def yztransform(ed):
        """gives the face vertexes coordinates in the inkscape format/translation (view xz)"""
        x1,y1,z1 = ed[0]
        x2,y2,z2 = ed[1]
        y1=-y1; y2=-y2
        z1=-(z1-maxZ-maxX-space)
        z2=-(z2-maxZ-maxX-space)
        return x1,y1,z1,x2,y2,z2

    def transform(ed, expview, scale):
        if expview=='xy':
            x1,y1,z1,x2,y2,z2 = xytransform(ed)
            x1 += OFFSET
            y1 += OFFSET
            x2 += OFFSET
            y2 += OFFSET
            return int(x1*scale),int(y1*scale),int(x2*scale),int(y2*scale)
        elif expview=='xz':
            x1,y1,z1,x2,y2,z2 = xztransform(ed)
            x1 += OFFSET
            z1 += OFFSET
            x2 += OFFSET
            z2 += OFFSET
            return int(x1*scale),int(z1*scale),int(x2*scale),int(z2*scale)
        elif expview=='yz':
            x1,y1,z1,x2,y2,z2 = yztransform(ed)
            z1 += OFFSET
            y1 += OFFSET
            z2 += OFFSET
            y2 += OFFSET
            return int(z1*scale),int(y1*scale),int(z2*scale),int(y2*scale)

    file.write('<g\n')
    file.write('inkscape:label="Layer %s"\n' % expview.upper())
    file.write('inkscape:groupmode="layer"\n')
    file.write('id="layer%s">\n' % expview)


    """Prints all the inkscape data (no header)"""
    tmp_edges = []
    for ed in edges:
        tmp_edges.append(transform(ed, expview, scale))
    edges = tmp_edges

    tmp_edges = []
    for edge in edges:
        tmp_edges.append(normalize(edge))
    edges = tmp_edges
    edges.sort()


    tmp_edges = []
    for edge in edges:
        if edge not in tmp_edges:
            tmp_edges.append(edge)
    edges = tmp_edges

    for edge in edges:
        file.write('<path\n')
        file.write('style="fill:none;fill-opacity:0.75000000000000000;fill-rule:evenodd;stroke:#ff0000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"\n')
        file.write('d="M %i,%i L %i,%i"\n' % edge)
        file.write('/>\n')


    file.write('</g>\n')

def writexy(edges, bounds, filename, scale, space):
    """writes the x-y view file exported"""

    file = open(filename, 'wb')
    inkscapeheader(file)
    figdata(file, edges, 'xy', bounds, scale, space)
    inkscapefooter(file)
    file.close()
    print 'Successfully exported ', Blender.sys.basename(filename)# + seconds

def writexz(edges, bounds, filename, scale, space):
    """writes the x-z view file exported"""
    #start = time.clock()
    file = open(filename, 'wb')
    inkscapeheader(file)
    figdata(file, edges, 'xz', bounds, scale, space)
    inkscapefooter(file)
    file.close()
    print 'Successfully exported ', Blender.sys.basename(filename)# + seconds

def writeyz(edges, bounds, filename, scale, space):
    """writes the y-z view file exported"""

    #start = time.clock()
    file = open(filename, 'wb')
    inkscapeheader(file)
    figdata(file, edges, 'yz', bounds, scale, space)
    inkscapefooter(file)
    file.close()
    #end = time.clock()
    #seconds = " in %.2f %s" % (end-start, "seconds")
    print 'Successfully exported ', Blender.sys.basename(filename)# + seconds

def writeall(edges, bounds, filename, scale=90, space=2.0):
    """writes all 3 views

    Every view is a combined object in the resulting inkscape. file."""

    maxX,maxY,maxZ,minX,minY,minZ = bounds

    file = open(filename, 'wb')

    inkscapeheader(file)
    file.write('<!-- upper view (7) -->\n')

    figdata(file, edges, 'xy', bounds, scale, space)
    file.write('<!-- bottom view (1) -->\n')

    figdata(file, edges, 'xz', bounds, scale, space)

    file.write('<!-- right view (3) -->\n')
    figdata(file, edges, 'yz', bounds, scale, space)

    inkscapefooter(file)
    file.close()
    print 'Successfully exported ', Blender.sys.basename(filename)# + seconds

import BPyMessages

def write_ui(filename):
    if filename.lower().endswith('.svg'): filename = filename[:-4]

    PREF_SEP= Draw.Create(0)
    PREF_SCALE= Draw.Create(90)
    PREF_SPACE= Draw.Create(2.0)

    block = [\
        ("Separate Files", PREF_SEP, "Export each view axis as a seperate file"),\
        ("Space: ", PREF_SPACE, 0.0, 10.0, "Space between views in blender units"),\
        ("Scale: ", PREF_SCALE, 10, 100000, "Scale, 1200 is a good default")]

    if not Draw.PupBlock("Export SVG", block):
        return

    edges = []
    bounds = collect_edges(edges)

    if PREF_SEP.val:
        writexy(edges, bounds, filename + '_XY.svg', PREF_SCALE.val, PREF_SPACE.val)
        writexz(edges, bounds, filename + '_XZ.svg', PREF_SCALE.val, PREF_SPACE.val)
        writeyz(edges, bounds, filename + '_YZ.svg', PREF_SCALE.val, PREF_SPACE.val)

    writeall(edges, bounds, filename + '.svg', PREF_SCALE.val, PREF_SPACE.val)

if __name__ == '__main__':
    Blender.Window.FileSelector(write_ui, 'Export INKSCAPE', Blender.sys.makename(ext='.svg'))

