"""Convert rhino geometry to compas geometry.

This script is a gh_python component script.
A grasshopper python component needs to be set as follow:

input parameters
----------
* rhino_geometry: no type hint, item access

output parameters
----------
* compas_geometry
"""

import Rhino.Geometry as r_g  # type: ignore # noqa: F401
import compas
import compas.datastructures as cd
import compas_rhino.geometry as crg

__author__ = 'ChiaChing Yen'
__email__ = '<ccyen@umich.edu>'


def convert_rhino_brep_to_compas_mesh(rhino_mesh):
    """Converts a Rhino brep to a COMPAS mesh.

    Parameters
    ----------
        rhino_brep (Rhino.Geometry.Brep): The rhino brep that will be converted

    Returns:
    ----------
        compas.datastructures.Mesh

    """

    rhino_mesh_vertice_list = rhino_mesh.Vertices
    rhino_mesh_faces_list = rhino_mesh.Faces

    # convert rhino.mesh.vertexCollection to generic tuples of float
    vertice_list = []

    for vertex in rhino_mesh_vertice_list:
        vertice_list.append((vertex.X, vertex.Y, vertex.Z))

    # convert rhino.mesh.MeshFaceCollection to generic tuples of int
    face_list = []
    for face in rhino_mesh_faces_list:
        if face.IsQuad:
            face_list.append((face.A, face.B, face.C, face.D))
        elif face.IsTriangle:
            face_list.append((face.A, face.B, face.C))

    compas_mesh = cd.Mesh.from_vertices_and_faces(vertice_list, face_list)

    return compas_mesh


def convert_rhino_geometry_to_compas_geometry(rhino_geometry):
    """Converts a Rhino point to a COMPAS point.

    Parameters
    ----------
        rhino_point (Any): The rhino geometry that will be converted

    Returns:
    ----------
        compas.geometry
    """
    if isinstance(rhino_geometry, r_g.Point3d):
        return crg.RhinoPoint.from_geometry(rhino_geometry).to_compas()
    elif isinstance(rhino_geometry, r_g.Vector3d):
        return crg.RhinoVector.from_geometry(rhino_geometry).to_compas()
    elif isinstance(rhino_geometry, r_g.Line):
        return crg.RhinoLine.from_geometry(rhino_geometry).to_compas()
    elif isinstance(rhino_geometry, r_g.Plane):
        return crg.RhinoPlane.from_geometry(rhino_geometry).to_compas()
    elif isinstance(rhino_geometry, r_g.Mesh):
        return crg.RhinoMesh.from_geometry(rhino_geometry).to_compas()
    elif isinstance(rhino_geometry, r_g.Brep):
        print("converting a rhino brep to compas mesh")
        return crg.RhinoMesh.from_geometry(rhino_geometry).to_compas()
    else:
        print("{0} is not supportted.".format(type(rhino_geometry)))
        raise TypeError


if __name__ == "__main__":
    if compas.is_ironpython() or compas.is_mono():
        if rg is not None:  # type: ignore # noqa: F823
            cg = convert_rhino_geometry_to_compas_geometry(rg)  # type: ignore # noqa: F823
