import os

import numpy as np
import itertools as it

from apeer_ometiff_library import omexmlClass

import skimage.util
from skimage.external import tifffile

def read_serie(serie, size_c, size_z, size_t):
    array = serie.asarray()

    # Expand image array to 5D of order (T, Z, C, X, Y)
    if size_c == 1:
        array = np.expand_dims(array, axis=-3)
    if size_z == 1:
        array = np.expand_dims(array, axis=-4)
    if size_t == 1:
        array = np.expand_dims(array, axis=-5)

    return array

def write_ometiff(output_path, array6D, omexml_string):
    with tifffile.TiffWriter(output_path) as tif:
        for i in range(len(array6D)):
            # check if this is the first Series
            if i != 0:
                # for other series, no need to add the omexml. The contiguous=False allows to add the series one by one to the same file
                tif.save(array6D[i], photometric='minisblack', metadata={'axes': 'TZCXY'}, contiguous=False)
            else:
                tif.save(array6D[i], description = omexml_string, photometric='minisblack', metadata={'axes': 'TZCXY'})

def apply_2d_transfo_to_serie(trafo_2d, array_5d, inputs, dtype=None):
    array_out_5d = np.zeros_like(array_5d)
    if dtype!=None:
        array_out_5d = array_out_5d.astype(dtype)
    n_t, n_z, n_c, n_x, n_y = np.shape(array_out_5d)

    for t, z, c in it.product(range(n_t), range(n_z), range(n_c)):
        array_out_5d[t, z, c, :, :] = trafo_2d(array_5d[t, z, c, :, :], inputs)

    return array_out_5d

def _invert(image2d, F):
    return skimage.util.invert(image2d, signed_float=F)

def execute(image_path):

    image_name = os.path.basename(image_path)
    print(image_name)

    with tifffile.TiffFile(image_path) as tif:

        array6D = []
        # Turn Ome XML String to a Bioformats object for parsing
        omexml = tif[0].image_description.decode("utf-8")
        metadata = omexmlClass.OMEXML(omexml)
        # Parse pixel sizes
        size_c = metadata.image(0).Pixels.SizeC
        size_z = metadata.image(0).Pixels.SizeZ
        size_t = metadata.image(0).Pixels.SizeT

        # Read each series, get the 5d array -> process it -> append to array6D
        for i in range(len(tif.series)):
            # Returned value is a 5D array of order (T, Z, C, X, Y)
            array5D = read_serie(tif.series[i], size_c, size_z, size_t)
            # Apply inversion operation
            result5d = apply_2d_transfo_to_serie(_invert, array5D, False)

            array6D.append(result5d)

    # Save the inverted image
    write_ometiff(image_name, array6D, omexml)

    print("INVERTION DONE")

    return {'output_image':image_name}

    # return {'output_image': image_name}

# Test code locally
if __name__ == "__main__":
    execute("/Users/olegsouzdalev/Desktop/ZEISS/Apeer/Database/Series.ome.tiff")