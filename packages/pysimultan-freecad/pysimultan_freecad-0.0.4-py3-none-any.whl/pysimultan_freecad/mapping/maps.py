from .mapper import mapper
# from . import method_mapper, view_manager
from .contents import contents
from PySimultan2.taxonomy_maps import TaxonomyMap

from ..freecad.fc_geometry import FreeCADGeometry, Assembly, Face as FCFace, Solid, Edge, Wire, Vertex, Feature


free_cad_geometry_map = TaxonomyMap(taxonomy_name='FreeCADGeometry',
                                    taxonomy_key='FreeCADGeometry',
                                    taxonomy_entry_name='FreeCADGeometry',
                                    taxonomy_entry_key='free_cad_geometry',
                                    content=[contents['geometry_file'],
                                             contents['uuid'],
                                             ]
                                    )

mapper.register(free_cad_geometry_map.taxonomy_entry_key, FreeCADGeometry, taxonomy_map=free_cad_geometry_map)
MappedFreeCADGeometry = mapper.get_mapped_class(free_cad_geometry_map.taxonomy_entry_key)


default_geo_content = [contents['txt_id'],
                       contents['uuid'],
                       contents['fc_obj_file'],
                       contents['fc_obj_file_id'],
                       ]


face_map = TaxonomyMap(taxonomy_name='FreeCAD',
                       taxonomy_key='FreeCAD',
                       taxonomy_entry_name='Face',
                       taxonomy_entry_key='face',
                       content=[*default_geo_content,
                                contents['normal'],
                                contents['_area'],
                                ],
                       )

mapper.register(face_map.taxonomy_entry_key, FCFace, taxonomy_map=face_map)
MappedFace = mapper.get_mapped_class(face_map.taxonomy_entry_key)


solid_map = TaxonomyMap(taxonomy_name='FreeCAD',
                        taxonomy_key='FreeCAD',
                        taxonomy_entry_name='Solid',
                        taxonomy_entry_key='solid',
                        content=[*default_geo_content,
                                 contents['_faces'],
                                 contents['features'],
                                 contents['volume'],
                                 contents['_is_closed']
                                 ],
                        )

mapper.register(solid_map.taxonomy_entry_key, Solid, taxonomy_map=solid_map)
MappedSolid = mapper.get_mapped_class(solid_map.taxonomy_entry_key)


assembly_map = TaxonomyMap(taxonomy_name='FreeCAD',
                           taxonomy_key='FreeCAD',
                           taxonomy_entry_name='Assembly',
                           taxonomy_entry_key='assembly',
                           content=[contents['txt_id'],
                                    contents['uuid'],
                                    contents['fc_obj_file'],
                                    contents['_features'],
                                    contents['_interfaces'],
                                    contents['comp_solid'],
                                    ],
                           )

mapper.register(assembly_map.taxonomy_entry_key, Assembly, taxonomy_map=assembly_map)
MappedAssembly = mapper.get_mapped_class(assembly_map.taxonomy_entry_key)


edge_map = TaxonomyMap(taxonomy_name='FreeCAD',
                       taxonomy_key='FreeCAD',
                       taxonomy_entry_name='Edge',
                       taxonomy_entry_key='edge',
                       content=[*default_geo_content,
                                contents['_length'],
                                contents['_vertices'],
                                ],
                       )

mapper.register(edge_map.taxonomy_entry_key, Edge, taxonomy_map=edge_map)
MappedEdge = mapper.get_mapped_class(edge_map.taxonomy_entry_key)

wire_map = TaxonomyMap(taxonomy_name='FreeCAD',
                       taxonomy_key='FreeCAD',
                       taxonomy_entry_name='Wire',
                       taxonomy_entry_key='wire',
                       content=[*default_geo_content,
                                contents['_length'],
                                contents['_is_closed'],
                                ],
                       )

mapper.register(wire_map.taxonomy_entry_key, Wire, taxonomy_map=wire_map)
MappedWire = mapper.get_mapped_class(wire_map.taxonomy_entry_key)

vertex_map = TaxonomyMap(taxonomy_name='FreeCAD',
                         taxonomy_key='FreeCAD',
                         taxonomy_entry_name='Vertex',
                         taxonomy_entry_key='vertex',
                         content=[*default_geo_content,
                                  ],
                         )
mapper.register(vertex_map.taxonomy_entry_key, Vertex, taxonomy_map=vertex_map)
MappedVertex = mapper.get_mapped_class(vertex_map.taxonomy_entry_key)


feature_map = TaxonomyMap(taxonomy_name='FreeCAD',
                          taxonomy_key='FreeCAD',
                          taxonomy_entry_name='Feature',
                          taxonomy_entry_key='feature',
                          content=[contents['fc_obj_file'],
                                   contents['fc_obj_file_id'],
                                   contents['uuid']
                                   ],
                          )

mapper.register(feature_map.taxonomy_entry_key, Feature, taxonomy_map=feature_map)
MappedFeature = mapper.get_mapped_class(feature_map.taxonomy_entry_key)
