import pathlib
import FreeCAD
import Part as FCPart

App = FreeCAD

import numpy as np
from FreeCAD import Base
# import DraftVecUtils

def export_objects(objects, filename, add_suffix=True):

    if not isinstance(objects, list):
        objects = [objects]

    file_suffix = pathlib.Path(filename).suffix

    doc = App.newDocument()

    for i, object in enumerate(objects):

        __o__ = doc.addObject("Part::Feature", f'{type(object).__name__}{i}')
        __o__.Label = f'{type(object).__name__}{i}'
        __o__.Shape = object

    if add_suffix:
        id = next(export_iter)
        p = pathlib.Path(filename)
        filename = "{0}_{2}{1}".format(pathlib.Path.joinpath(p.parent, p.stem), p.suffix, id)

    if file_suffix == '.FCStd':
        doc.recompute()
        doc.saveCopy(filename)
    else:
        FCPart.export(doc.Objects, filename)


# def angle_between_vectors(v1: Base.Vector,
#                           v2: Base.Vector,
#                           normal: Base.Vector = None,
#                           deg=True):
#
#     if normal is None:
#         angle = DraftVecUtils.angle(v1.normalize(), v2.normalize())
#     else:
#         angle = DraftVecUtils.angle(v1.normalize(), v2.normalize(), normal)
#     if not deg:
#         return angle
#     return np.rad2deg(angle)
