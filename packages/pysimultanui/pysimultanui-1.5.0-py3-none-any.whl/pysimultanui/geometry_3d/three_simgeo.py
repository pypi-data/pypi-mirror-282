import sys
import traceback
from typing import Any, Optional, List, Union
from .scene import ExtendedScene
import numpy as np

import logging

from SIMULTAN.Data.Geometry import (Layer, Vertex, Edge, PEdge, Face, Volume, EdgeLoop, OperationPermission,
                                             GeometryModelOperationPermissions, GeometryOperationPermissions,
                                             LayerOperationPermissions, GeometryModelData, GeometricOrientation,
                                             BaseEdgeContainer)

from PySimultan2.geometry.geometry_base import (SimultanVolume, SimultanFace, SimultanEdge, SimultanVertex,
                                                SimultanLayer, SimultanEdgeLoop, GeometryModel)



logger = logging.getLogger('PySimultanUI')


def rgb_to_hex(rgb: List[int]) -> str:
    if rgb is None:
        return '#000000'
    return f'#{rgb[0] << 16 | rgb[1] << 8 | rgb[2]:06x}'


# def display_vertices(vertices: List[FCPart.Vertex],
#                      scene: ExtendedScene,
#                      obj_id: str = '',
#                      colors: list[list[int]] = None):
#
#     try:
#         if colors is None:
#             colors = [[0, 0, 0]] * vertices.__len__()
#
#         point_cloud = scene.point_cloud([list(x.Point) for x in vertices],
#                                         colors=colors,
#                                         point_size=0.1).with_name(obj_id)
#     except Exception as e:
#         logger.error(f'Error displaying vertices: {e}\n'
#                      f'{traceback.format_exception(*sys.exc_info())}')
#         point_cloud = None
#
#     return point_cloud
#
#
# def display_edges(edges: Union[List[FCPart.Edge], FCPart.Edge],
#                   scene: ExtendedScene,
#                   obj_id: str = '',
#                   color: Optional[list[int]] = None):
#
#     rgb_color = rgb_to_hex(color)
#
#     if isinstance(edges, FCPart.Edge):
#         edges = [edges]
#
#     objects3d = []
#
#     for edge in edges:
#         try:
#             if edge.Curve.TypeId == 'Part::GeomLine':
#                 objects3d.append(scene.line(list(edge.Vertexes[0].Point),
#                                             list(edge.Vertexes[1].Point)).material(rgb_color).with_name(obj_id))
#             else:
#
#                 n_points = int(edge.Length / 100) + 1
#                 if n_points < 100:
#                     n_points = 100
#                 elif n_points > 1000:
#                     n_points = 1000
#
#                 wire_vertices = np.array(list(edge.discretize(n_points)))
#                 objects3d.append(scene.wire(wire_vertices).material(rgb_color).with_name(obj_id))
#         except Exception as e:
#             logger.error(f'Error displaying edges: {e}\n'
#                          f'{traceback.format_exception(*sys.exc_info())}')
#
#     return objects3d
#
#
# def display_wire(wire: FCPart.Wire,
#                  scene: ExtendedScene,
#                  obj_id: str = '',
#                  color: Optional[list[int]] = None):
#
#     try:
#         return display_edges(wire.Edges, scene, obj_id, color)
#     except Exception as e:
#         logger.error(f'Error displaying wire: {e}\n'
#                      f'{traceback.format_exception(*sys.exc_info())}')
#
#
# def display_face(face: FCPart.Face,
#                  scene: ExtendedScene,
#                  obj_id: str = '',
#                  color: Optional[list[int]] = None):
#
#     try:
#         rgb_color = rgb_to_hex(color)
#         tris = face.tessellate(5, True)
#         return scene.mesh(np.array(tris[0]),
#                           np.array(tris[1])
#                           ).material(rgb_color).with_name(obj_id)
#     except Exception as e:
#         logger.error(f'Error displaying face: {e}\n'
#                      f'{traceback.format_exception(*sys.exc_info())}')
#
#
# def display_solid(solid: FCPart.Solid,
#                   scene: ExtendedScene,
#                   obj_id: str = '',
#                   color: Optional[list[int]] = None):
#     try:
#         rgb_color = rgb_to_hex(color)
#         tris = solid.tessellate(5, True)
#
#         return scene.mesh(np.array(tris[0]),
#                           np.array(tris[1])
#                           ).material(rgb_color).with_name(obj_id)
#     except Exception as e:
#         logger.error(f'Error displaying solid: {e}\n'
#                      f'{traceback.format_exception(*sys.exc_info())}')


def display_simgeo(simgeo: Union[Layer, Vertex, Edge, PEdge, Face, Volume, EdgeLoop],
                   scene: ExtendedScene,
                   obj_id: str = '',
                   color: Optional[list[int]] = None):
    try:

        with scene.group() as group:
            rgb_color = rgb_to_hex([simgeo._wrapped_object.Color.Color.R,
                                    simgeo._wrapped_object.Color.Color.G,
                                    simgeo._wrapped_object.Color.Color.B])

            if isinstance(simgeo, SimultanVertex):
                scene.point_cloud([simgeo.position],
                                  colors=[[simgeo._wrapped_object.Color.Color.R,
                                           simgeo._wrapped_object.Color.Color.G,
                                           simgeo._wrapped_object.Color.Color.B]],
                                  point_size=0.1).with_name(simgeo.id)
            elif isinstance(simgeo, SimultanEdge):
                scene.line(simgeo.vertex_0.position,
                           simgeo.vertex_1.position).material(rgb_color).with_name(simgeo.id)
            elif isinstance(simgeo, SimultanFace):
                tris = simgeo.triangulate()
                scene.mesh(tris[0], tris[1]).material(rgb_color).with_name(simgeo.id)
            elif isinstance(simgeo, SimultanVolume):
                for face in simgeo.faces:
                    tris = face.triangulate()
                    scene.mesh(tris[0], tris[1]).material(rgb_color).with_name(simgeo.id)

            return group

    except Exception as e:
        logger.error(f'Error displaying simgeo: {e}\n'
                     f'{traceback.format_exception(*sys.exc_info())}')
