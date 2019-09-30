from plumbum import local


def execute(image_path, keys):

    print('IMAGE_PATH', image_path)

    output_file = './6D_converted.ome.tiff'
    bfconvert = local['bfconvert']
    if len(keys) != 0:
        bashCommand = bfconvert[keys.split(' '), image_path, output_file]
    else:
        bashCommand = bfconvert[image_path, output_file]
    print("RUNNING COMMAND ", bashCommand)
    bashCommand()

    return {'output_image': output_file}

if __name__ == "__main__":
    execute('./input/6D_image.czi', '')