"""Convert compas geometry to Rhino geometry.

This script is a gh_python component script.
A grasshopper python component needs to be set as follow:

input parameters
----------
* compas_geometry: no type hint, item access

output parameters
----------
* rhino_geometry
"""

import compas.datastructures as cd
import compas.geometry as cg
import compas_ghpython.artists as cgha
import compas
import Rhino.Geometry as rg  # type: ignore #noqa: F401

__author__ = 'ChiaChing Yen'
__email__ = '<ccyen@umich.edu>'

def ct2rt(ct):
    """Converts a compas transformation to a Rhino.Grasshopper transformation.
    """
    t = rg.Transform(1)
    t.M00 = ct.list[0]
    t.M01 = ct.list[1]
    t.M02 = ct.list[2]
    t.M03 = ct.list[3]
    t.M10 = ct.list[4]
    t.M11 = ct.list[5]
    t.M12 = ct.list[6]
    t.M13 = ct.list[7]
    t.M20 = ct.list[8]
    t.M21 = ct.list[9]
    t.M22 = ct.list[10]
    t.M23 = ct.list[11]
    t.M30 = ct.list[12]
    t.M31 = ct.list[13]
    t.M32 = ct.list[14]
    t.M33 = ct.list[15]

    return t


def convert_compas_geometry_to_gh_geometry(compas_geometry):
    """Converts a compas geometry to a Rhino.Grasshopper geometry.

    Parameters
    ----------
        compas_geometry (Any): The compas geometry that will be converted

    Returns:
    ----------
        Rhino.Geometry
    """
    if isinstance(compas_geometry, cg.Point):
        return cgha.PointArtist(compas_geometry).draw()
    elif isinstance(compas_geometry, cg.Vector):
        return rg.Vector3d(compas_geometry.x, compas_geometry.y, compas_geometry.z)
    elif isinstance(compas_geometry, cg.Line):
        return cgha.LineArtist(compas_geometry).draw()
    elif isinstance(compas_geometry, cg.Frame):
        return cgha.FrameArtist(compas_geometry, scale=100).draw()
    elif isinstance(compas_geometry, cg.Plane):
        return cgha.FrameArtist(cg.Frame.from_plane(compas_geometry), scale=100).draw()
    elif isinstance(compas_geometry, cd.Mesh):
        return cgha.MeshArtist(compas_geometry).draw()
    elif isinstance(compas_geometry, cg.Polyline):
        return cgha.PolylineArtist(compas_geometry).draw()
    elif isinstance(compas_geometry, cg.Transform):
        return ct2rt(compas_geometry)
    else:
        print("{0} is not supportted.".format(type(compas_geometry)))
        raise TypeError


if __name__ == "__main__":
    if compas.is_ironpython() or compas.is_mono():
        if compas_geometry is not None:  # type: ignore # noqa: F823
            rhino_geometry = convert_compas_geometry_to_gh_geometry(compas_geometry)  # type: ignore # noqa: F823
