from PySimultan2.taxonomy_maps import Content

contents = dict()

attributes = [
    ('solids', 'solids', None, None, 'Solids'),
    ('features', 'features', None, None, 'Features'),
    ('interfaces', '_interfaces', None, None, 'Interfaces'),
    ('topology', 'topology', None, None, 'Topology'),
    ('comp_solid', 'comp_solid', None, None, 'Comp solid'),
    ('assembly', 'assembly', None, None, 'Assembly'),
    ('geometry_file', 'geometry_file', None, None, 'Geometry file'),
    ('fc_inst', '_fc_inst', None, None, 'FreeCAD instance'),
    ('normal', '_normal', None, None, 'Normal'),
    ('fc_obj_file', 'fc_obj_file', None, None, 'FreeCAD file object'),
    ('fc_obj_file_id', 'fc_obj_file_id', int, None, 'FreeCAD file object id'),
    ('txt_id', '_txt_id', None, None, 'Text id'),
    ('features', 'features', None, None, 'Features'),
    ('uuid', 'uuid', None, None, 'UUID'),
    ('volume', '_volume', float, 'm^3', 'Volume'),
]

# Populate contents dictionary
for attr_name, property_name, attr_type, unit, description in attributes:
    contents[attr_name] = Content(
        text_or_key=attr_name,
        property_name=property_name,
        type=attr_type,
        unit=unit,
        documentation=description
    )


contents['_features'] = Content(text_or_key='features',
                                property_name='_features',
                                type=None,
                                unit='',
                                documentation='')

contents['_interfaces'] = Content(text_or_key='interfaces',
                                  property_name='_interfaces',
                                  type=None,
                                  unit='',
                                  documentation='')

contents['_faces'] = Content(text_or_key='faces',
                             property_name='_faces',
                             type=None,
                             unit='',
                             documentation='')

contents['_area'] = Content(text_or_key='area',
                            property_name='_area',
                            type=None,
                            unit='',
                            documentation='')

contents['_length'] = Content(text_or_key='length',
                              property_name='_length',
                              type=None,
                              unit='',
                              documentation='')

contents['_is_closed'] = Content(text_or_key='is_closed',
                                 property_name='_is_closed',
                                 type=None,
                                 unit='',
                                 documentation='')

contents['_vertices'] = Content(text_or_key='vertices',
                                property_name='_vertices',
                                type=None,
                                unit='',
                                documentation='')
