import sys
import traceback
import random
from logging import getLogger
from typing import TYPE_CHECKING, Optional

import FreeCAD
import MeshPart
import Part as FCPart
from PySimultan2.geometry.geometry_base import (GeometryModel, SimultanVertex, SimultanEdge, SimultanEdgeLoop,
                                                SimultanFace, SimultanVolume, SimultanLayer)

if TYPE_CHECKING:
    from PySimultan2.data_model import DataModel
    from PySimultan2.object_mapper import PythonMapper

logger = getLogger('PySimultan-FreeCAD-Tools')
logger.setLevel('DEBUG')


def vertex_from_freecad(vertex: FCPart.Vertex,
                        layer: SimultanLayer,
                        vertex_lookup: Optional[dict[FCPart.Vertex, SimultanVertex]] = None,
                        vertex_pos_lookup: Optional[dict[tuple[float, float, float], SimultanVertex]] = None,
                        scale: float = 1.0,
                        feature: Optional[FCPart.Feature] = None,
                        ) -> SimultanVertex:

    if vertex_lookup is None:
        vertex_lookup = {}
    if vertex_pos_lookup is None:
        vertex_pos_lookup = {}

    if vertex in vertex_lookup:
        return vertex_lookup[vertex]
    elif (vertex.X * scale, vertex.Y * scale, vertex.Z * scale) in vertex_pos_lookup:
        return vertex_pos_lookup[(vertex.X * scale, vertex.Y * scale, vertex.Z * scale)]

    new_vertex = SimultanVertex(name=f'{feature.Name} {feature.Label}' if feature is not None else 'Vertex',
                                x=vertex.X * scale,
                                y=vertex.Y * scale,
                                z=vertex.Z * scale,
                                layer=layer)
    vertex_pos_lookup[(vertex.X * scale,
                       vertex.Y * scale,
                       vertex.Z * scale)] = new_vertex
    vertex_lookup[vertex] = new_vertex
    return new_vertex


def edge_from_freecad(edge: FCPart.Edge,
                      layer: SimultanLayer,
                      vertex_lookup: Optional[dict[FCPart.Vertex, SimultanVertex]] = None,
                      vertex_pos_lookup: Optional[dict[tuple[float, float, float], SimultanVertex]] = None,
                      edge_lookup: Optional[dict[FCPart.Edge, SimultanEdge]] = None,
                      edge_v_lookup: Optional[dict[tuple[SimultanVertex, SimultanVertex], SimultanEdge]] = None,
                      feature: Optional[FCPart.Feature] = None,
                      max_length: float = 10.0,
                      ) -> SimultanEdge:

    if isinstance(edge.Curve, FCPart.Line):
        if edge in edge_lookup:
            return edge_lookup[edge]
        elif (edge.Vertexes[0], edge.Vertexes[1]) in edge_v_lookup:
            return edge_v_lookup[(edge.Vertexes[0], edge.Vertexes[1])]

        new_edge = SimultanEdge(name=f'{feature.Name} {feature.Label}' if feature is not None else 'Edge',
                                vertices=[vertex_from_freecad(edge.Vertexes[0],
                                                              vertex_lookup=vertex_lookup,
                                                              vertex_pos_lookup=vertex_pos_lookup,
                                                              scale=1.0,
                                                              layer=layer),
                                          vertex_from_freecad(edge.Vertexes[1],
                                                              vertex_lookup=vertex_lookup,
                                                              vertex_pos_lookup=vertex_pos_lookup,
                                                              scale=1.0,
                                                              layer=layer)],
                                layer=layer)
        edge_lookup[edge] = new_edge
        edge_v_lookup[(edge.Vertexes[0], edge.Vertexes[1])] = new_edge

        return new_edge

    else:
        if edge in edge_lookup:
            return edge_lookup[edge]

        pts = edge.discretize(int(edge.Length/max_length) + 1)

        edges = [SimultanEdge(name=f'{feature.Name} {feature.Label}' if feature is not None else 'Edge',
                              vertices=[vertex_from_freecad(FCPart.Vertex(pts[i]),
                                                            vertex_lookup=vertex_lookup,
                                                            vertex_pos_lookup=vertex_pos_lookup,
                                                            scale=1.0,
                                                            layer=layer),
                                        vertex_from_freecad(FCPart.Vertex(pts[i+1]),
                                                            vertex_lookup=vertex_lookup,
                                                            vertex_pos_lookup=vertex_pos_lookup,
                                                            scale=1.0,
                                                            layer=layer)
                                        ],
                              layer=layer) for i in range(len(pts) - 1)]

        edge_lookup[edge] = edges
        return edges


def wire_from_freecad(wire: FCPart.Wire,
                      layer: SimultanLayer,
                      vertex_lookup: Optional[dict[FCPart.Vertex, SimultanVertex]] = None,
                      vertex_pos_lookup: Optional[dict[tuple[float, float, float], SimultanVertex]] = None,
                      edge_lookup: Optional[dict[FCPart.Edge, SimultanEdge]] = None,
                      edge_v_lookup: Optional[dict[tuple[SimultanVertex, SimultanVertex], SimultanEdge]] = None,
                      wire_lookup: Optional[dict[FCPart.Wire, SimultanEdgeLoop]] = None,
                      wire_e_lookup: Optional[dict[tuple[SimultanEdge], SimultanEdgeLoop]] = None,
                      feature: Optional[FCPart.Feature] = None,
                      max_length: float = 10.0,
                      ) -> SimultanEdgeLoop:

    if wire_lookup is None:
        wire_lookup = {}

    if wire_e_lookup is None:
        wire_e_lookup = {}

    if wire in wire_lookup:
        return wire_lookup[wire]

    edges = []

    for edge in wire.OrderedEdges:
        simultan_edge = edge_from_freecad(edge,
                                          layer=layer,
                                          vertex_lookup=vertex_lookup,
                                          vertex_pos_lookup=vertex_pos_lookup,
                                          edge_lookup=edge_lookup,
                                          edge_v_lookup=edge_v_lookup,
                                          feature=feature,
                                          max_length=max_length,
                                          )
        if isinstance(simultan_edge, list):
            edges.extend(simultan_edge)
        else:
            edges.append(simultan_edge)

    # edges = [edge_from_freecad(edge,
    #                            layer=layer,
    #                            vertex_lookup=vertex_lookup,
    #                            vertex_pos_lookup=vertex_pos_lookup,
    #                            edge_lookup=edge_lookup,
    #                            edge_v_lookup=edge_v_lookup,
    #                            max_length=max_length,
    #                            ) for edge in wire.OrderedEdges]

    if tuple(edges) in wire_e_lookup:
        return wire_e_lookup[tuple(edges)]

    try:
        new_wire = SimultanEdgeLoop(name=f'{feature.Name} {feature.Label}' if feature is not None else 'Wire',
                                    edges=edges,
                                    layer=layer)
    except Exception as e:
        print('\n')
        print('\n'.join([str([x.vertex_0, x.vertex_1]) for x in edges]))
        print('\n')

        raise e
    wire_lookup[wire] = new_wire
    wire_e_lookup[tuple(edges)] = new_wire

    return new_wire


def face_from_freecad(face: FCPart.Face,
                      layer: SimultanLayer,
                      vertex_lookup: Optional[dict[FCPart.Vertex, SimultanVertex]] = None,
                      vertex_pos_lookup: Optional[dict[tuple[float, float, float], SimultanVertex]] = None,
                      edge_lookup: Optional[dict[FCPart.Edge, SimultanEdge]] = None,
                      edge_v_lookup: Optional[dict[tuple[SimultanVertex, SimultanVertex], SimultanEdge]] = None,
                      wire_lookup: Optional[dict[FCPart.Wire, SimultanEdgeLoop]] = None,
                      wire_e_lookup: Optional[dict[tuple[SimultanEdge], SimultanEdgeLoop]] = None,
                      face_lookup: Optional[dict[FCPart.Face, SimultanFace]] = None,
                      face_w_lookup: Optional[dict[tuple[SimultanEdgeLoop], SimultanFace]] = None,
                      feature: Optional[FCPart.Feature] = None,
                      max_length: float = 10.0,
                      ) -> SimultanFace:

    if not isinstance(face.Surface, FCPart.Plane):
        mesh_shp = MeshPart.meshFromShape(face,
                                          Fineness=2,
                                          SecondOrder=0,
                                          Optimize=1,
                                          AllowQuad=1)

        faces = [None] * len(mesh_shp.Facets)
        for i, facet in enumerate(mesh_shp.Facets):
            # create a face for each facet
            fc_face = FCPart.Face(FCPart.makePolygon([*facet.Points, facet.Points[0]]))
            faces[i] = face_from_freecad(fc_face,
                                         layer=layer,
                                         vertex_lookup=vertex_lookup,
                                         vertex_pos_lookup=vertex_pos_lookup,
                                         edge_lookup=edge_lookup,
                                         edge_v_lookup=edge_v_lookup,
                                         wire_lookup=wire_lookup,
                                         wire_e_lookup=wire_e_lookup,
                                         face_lookup=face_lookup,
                                         face_w_lookup=face_w_lookup,
                                         max_length=max_length,
                                         )
        return faces

    else:
        if face_lookup is None:
            face_lookup = {}

        if face_w_lookup is None:
            face_w_lookup = {}

        if face in face_lookup:
            return face_lookup[face]

        wires = [wire_from_freecad(wire,
                                   layer=layer,
                                   vertex_lookup=vertex_lookup,
                                   vertex_pos_lookup=vertex_pos_lookup,
                                   edge_lookup=edge_lookup,
                                   edge_v_lookup=edge_v_lookup,
                                   wire_lookup=wire_lookup,
                                   wire_e_lookup=wire_e_lookup,
                                   ) for wire in face.Wires]

        if tuple(wires) in face_w_lookup:
            return face_w_lookup[tuple(wires)]

        boundary_edge_loop = wire_from_freecad(face.OuterWire,
                                               layer=layer,
                                               vertex_lookup=vertex_lookup,
                                               vertex_pos_lookup=vertex_pos_lookup,
                                               edge_lookup=edge_lookup,
                                               edge_v_lookup=edge_v_lookup,
                                               wire_lookup=wire_lookup,
                                               wire_e_lookup=wire_e_lookup,
                                               max_length=max_length,
                                               )
        holes = [wire_from_freecad(x,
                                   layer=layer,
                                   vertex_lookup=vertex_lookup,
                                   vertex_pos_lookup=vertex_pos_lookup,
                                   edge_lookup=edge_lookup,
                                   edge_v_lookup=edge_v_lookup,
                                   wire_lookup=wire_lookup,
                                   wire_e_lookup=wire_e_lookup,
                                   max_length=max_length,
                                   ) for x in [x for x in face.Wires if not x.isEqual(face.OuterWire)]]

        if holes:
            logger.debug(f'Face has holes: {holes}')

        new_face = SimultanFace(name=f'{feature.Name} {feature.Label}' if feature is not None else 'Face',
                                edge_loop=boundary_edge_loop,
                                holes=holes,
                                layer=layer)

        new_face._wrapped_object.Color.set_Color(new_face._wrapped_object.Color.
                                                 Color.FromRgb(random.randint(0, 255),
                                                               random.randint(0, 255),
                                                               random.randint(0, 255)
                                                               )
                                                 )
        face_lookup[face] = new_face
        face_w_lookup[tuple(wires)] = new_face
        return new_face


def volume_from_freecad(volume: FCPart.Solid,
                        layer: SimultanLayer,
                        vertex_lookup: Optional[dict[FCPart.Vertex, SimultanVertex]] = None,
                        vertex_pos_lookup: Optional[dict[tuple[float, float, float], SimultanVertex]] = None,
                        edge_lookup: Optional[dict[FCPart.Edge, SimultanEdge]] = None,
                        edge_v_lookup: Optional[dict[tuple[SimultanVertex, SimultanVertex], SimultanEdge]] = None,
                        wire_lookup: Optional[dict[FCPart.Wire, SimultanEdgeLoop]] = None,
                        wire_e_lookup: Optional[dict[tuple[SimultanEdge], SimultanEdgeLoop]] = None,
                        face_lookup: Optional[dict[FCPart.Face, SimultanFace]] = None,
                        face_w_lookup: Optional[dict[tuple[SimultanEdgeLoop], SimultanFace]] = None,
                        volume_lookup: Optional[dict[FCPart.Solid, SimultanVolume]] = None,
                        feature: Optional[FCPart.Feature] = None,
                        max_length: float = 10.0,
                        ) -> SimultanVolume:

    if volume_lookup is None:
        volume_lookup = {}

    if volume in volume_lookup:
        return volume_lookup[volume]

    faces = []
    for face in volume.Faces:
        new_face = face_from_freecad(face,
                                     layer=layer,
                                     vertex_lookup=vertex_lookup,
                                     vertex_pos_lookup=vertex_pos_lookup,
                                     edge_lookup=edge_lookup,
                                     edge_v_lookup=edge_v_lookup,
                                     wire_lookup=wire_lookup,
                                     wire_e_lookup=wire_e_lookup,
                                     face_lookup=face_lookup,
                                     face_w_lookup=face_w_lookup,
                                     max_length=max_length,
                                     )
        if isinstance(new_face, list):
            faces.extend(new_face)
        else:
            faces.append(new_face)

    new_volume = SimultanVolume(name=f'{feature.Name} {feature.Label}' if feature is not None else 'Volume',
                                faces=faces,
                                layer=layer)

    volume_lookup[volume] = new_volume
    return new_volume


def import_freecad(doc: FreeCAD.Document,
                   geo_model: GeometryModel,
                   data_model: Optional['DataModel'] = None,
                   object_mapper: Optional['PythonMapper'] = None,
                   scale: float=1.0) -> tuple[int, int, int, int, int]:

    vertex_lookup: dict[FCPart.Vertex: SimultanVertex] = {}
    vertex_pos_lookup: dict[tuple[float, float, float]: SimultanVertex] = {}
    edge_lookup: dict[FCPart.Edge: SimultanEdge] = {}
    edge_v_lookup: dict[tuple[SimultanVertex, SimultanVertex]: SimultanEdge] = {}
    wire_lookup: dict[FCPart.Wire: SimultanEdgeLoop] = {}
    wire_e_lookup: dict[tuple[SimultanEdge]: SimultanEdgeLoop] = {}
    face_lookup: dict[FCPart.Face: SimultanFace] = {}
    face_w_lookup: dict[tuple[SimultanEdgeLoop]: SimultanFace] = {}
    volume_lookup: dict[FCPart.Volume: SimultanVolume] = {}

    layer = SimultanLayer(name='Layer 1',
                          geometry_model=geo_model,
                          data_model=data_model if data_model is not None else geo_model._data_model,
                          object_mapper=object_mapper if object_mapper is not None else geo_model._object_mapper)

    for feature in doc.Objects:
        try:
            if isinstance(feature.Shape, FCPart.Vertex):
                vertex = vertex_from_freecad(feature,
                                             layer=layer,
                                             vertex_lookup=vertex_lookup,
                                             vertex_pos_lookup=vertex_pos_lookup,
                                             scale=scale)
            elif isinstance(feature.Shape, FCPart.Edge):
                edge = edge_from_freecad(feature,
                                         layer=layer,
                                         vertex_lookup=vertex_lookup,
                                         vertex_pos_lookup=vertex_pos_lookup,
                                         edge_lookup=edge_lookup,
                                         edge_v_lookup=edge_v_lookup)
            elif isinstance(feature.Shape, FCPart.Wire):
                wire = wire_from_freecad(feature.Shape,
                                         layer=layer,
                                         vertex_lookup=vertex_lookup,
                                         vertex_pos_lookup=vertex_pos_lookup,
                                         edge_lookup=edge_lookup,
                                         edge_v_lookup=edge_v_lookup,
                                         wire_lookup=wire_lookup,
                                         wire_e_lookup=wire_e_lookup,
                                         )
            elif isinstance(feature.Shape, FCPart.Face):
                face = face_from_freecad(feature.Shape,
                                         layer=layer,
                                         vertex_lookup=vertex_lookup,
                                         vertex_pos_lookup=vertex_pos_lookup,
                                         edge_lookup=edge_lookup,
                                         edge_v_lookup=edge_v_lookup,
                                         wire_lookup=wire_lookup,
                                         wire_e_lookup=wire_e_lookup,
                                         face_lookup=face_lookup,
                                         face_w_lookup=face_w_lookup,
                                         )
            elif isinstance(feature.Shape, FCPart.Solid):
                volume = volume_from_freecad(feature.Shape,
                                             layer=layer,
                                             vertex_lookup=vertex_lookup,
                                             vertex_pos_lookup=vertex_pos_lookup,
                                             edge_lookup=edge_lookup,
                                             edge_v_lookup=edge_v_lookup,
                                             wire_lookup=wire_lookup,
                                             wire_e_lookup=wire_e_lookup,
                                             face_lookup=face_lookup,
                                             face_w_lookup=face_w_lookup,
                                             volume_lookup=volume_lookup,
                                             )
        except Exception as e:
            print(f'Error processing feature: {e}')
            continue

    return (vertex_lookup.__len__(), edge_lookup.__len__(),
            wire_lookup.__len__(), face_lookup.__len__(), volume_lookup.__len__())


def import_feature(feature: FCPart.Feature,
                   layer: SimultanLayer,
                   scale: float = 1.0,
                   vertex_lookup: dict[FCPart.Vertex: SimultanVertex] = None,
                   vertex_pos_lookup: dict[tuple[float, float, float]: SimultanVertex] = None,
                   edge_lookup: dict[FCPart.Edge: SimultanEdge] = None,
                   edge_v_lookup: dict[tuple[SimultanVertex, SimultanVertex]: SimultanEdge] = None,
                   wire_lookup: dict[FCPart.Wire: SimultanEdgeLoop] = None,
                   wire_e_lookup: dict[tuple[SimultanEdge]: SimultanEdgeLoop] = None,
                   face_lookup: dict[FCPart.Face: SimultanFace] = None,
                   face_w_lookup: dict[tuple[SimultanEdgeLoop]: SimultanFace] = None,
                   volume_lookup: dict[FCPart.Solid: SimultanVolume] = None,
                   max_length: float = 10.0,
                   ):

    if vertex_lookup is None:
        vertex_lookup = {}
    if vertex_pos_lookup is None:
        vertex_pos_lookup = {}
    if edge_lookup is None:
        edge_lookup = {}
    if edge_v_lookup is None:
        edge_v_lookup = {}
    if wire_lookup is None:
        wire_lookup = {}
    if wire_e_lookup is None:
        wire_e_lookup = {}
    if face_lookup is None:
        face_lookup = {}
    if face_w_lookup is None:
        face_w_lookup = {}
    if volume_lookup is None:
        volume_lookup = {}

    try:
        logger.info(f'Feature is instance of {type(feature.Shape)}')
        if isinstance(feature.Shape, FCPart.Vertex):
            try:
                logger.info(f'Creating vertex from {feature.Name} {feature.Label}')
                vertex = vertex_from_freecad(feature.Shape,
                                             layer=layer,
                                             vertex_lookup=vertex_lookup,
                                             vertex_pos_lookup=vertex_pos_lookup,
                                             feature=feature,
                                             scale=scale)
            except Exception as e:
                logger.error(f'Error creating vertex: {e}'
                             f'\n{traceback.format_exception(*sys.exc_info())}')
                print(f'Error creating vertex: {e}'
                      f'\n{traceback.format_exception(*sys.exc_info())}')
                raise e
        elif isinstance(feature.Shape, FCPart.Edge):
            try:
                logger.info(f'Creating edge from {feature.Name} {feature.Label}')
                edge = edge_from_freecad(feature.Shape,
                                         layer=layer,
                                         vertex_lookup=vertex_lookup,
                                         vertex_pos_lookup=vertex_pos_lookup,
                                         edge_lookup=edge_lookup,
                                         edge_v_lookup=edge_v_lookup,
                                         feature=feature,
                                         max_length=max_length,)
            except Exception as e:
                logger.error(f'Error creating edge: {e}'
                             f'\n{traceback.format_exception(*sys.exc_info())}')
                print(f'Error creating edge: {e}'
                      f'\n{traceback.format_exception(*sys.exc_info())}')
                raise e
        elif isinstance(feature.Shape, FCPart.Wire):
            try:
                logger.info(f'Creating wire from {feature.Name} {feature.Label}')
                wire = wire_from_freecad(feature.Shape,
                                         layer=layer,
                                         vertex_lookup=vertex_lookup,
                                         vertex_pos_lookup=vertex_pos_lookup,
                                         edge_lookup=edge_lookup,
                                         edge_v_lookup=edge_v_lookup,
                                         wire_lookup=wire_lookup,
                                         wire_e_lookup=wire_e_lookup,
                                         feature=feature,
                                         max_length=max_length,
                                         )
            except Exception as e:
                logger.error(f'Error creating wire: {e}'
                             f'\n{traceback.format_exception(*sys.exc_info())}')
                print(f'Error creating wire: {e}'
                      f'\n{traceback.format_exception(*sys.exc_info())}')
                raise e
        elif isinstance(feature.Shape, FCPart.Face):
            try:
                logger.info(f'Creating face from {feature.Name} {feature.Label}')
                face = face_from_freecad(feature.Shape,
                                         layer=layer,
                                         vertex_lookup=vertex_lookup,
                                         vertex_pos_lookup=vertex_pos_lookup,
                                         edge_lookup=edge_lookup,
                                         edge_v_lookup=edge_v_lookup,
                                         wire_lookup=wire_lookup,
                                         wire_e_lookup=wire_e_lookup,
                                         face_lookup=face_lookup,
                                         face_w_lookup=face_w_lookup,
                                         feature=feature,
                                         max_length=max_length,
                                         )
            except Exception as e:
                logger.error(f'Error creating face: {e}'
                             f'\n{traceback.format_exception(*sys.exc_info())}')
                print(f'Error creating face: {e}'
                      f'\n{traceback.format_exception(*sys.exc_info())}')
                raise e
        elif isinstance(feature.Shape, FCPart.Solid):
            try:
                logger.info(f'Creating solid from {feature.Name} {feature.Label}')
                volume = volume_from_freecad(feature.Shape,
                                             layer=layer,
                                             vertex_lookup=vertex_lookup,
                                             vertex_pos_lookup=vertex_pos_lookup,
                                             edge_lookup=edge_lookup,
                                             edge_v_lookup=edge_v_lookup,
                                             wire_lookup=wire_lookup,
                                             wire_e_lookup=wire_e_lookup,
                                             face_lookup=face_lookup,
                                             face_w_lookup=face_w_lookup,
                                             volume_lookup=volume_lookup,
                                             feature=feature,
                                             max_length=max_length,
                                             )
            except Exception as e:
                logger.error(f'Error creating volume: {e}'
                             f'\n{traceback.format_exception(*sys.exc_info())}')
                print(f'Error creating volume: {e}'
                      f'\n{traceback.format_exception(*sys.exc_info())}')
                raise e
    except Exception as e:
        print(f'Error processing feature: {e}')
