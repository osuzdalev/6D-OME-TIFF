from apeer_dev_kit import adk
import invert_6D


if __name__ == "__main__":
    inputs = adk.get_inputs()

    outputs = invert_6D.execute(inputs['input_image'])

    adk.set_file_output('output_image', outputs['output_image'])
    adk.finalize()