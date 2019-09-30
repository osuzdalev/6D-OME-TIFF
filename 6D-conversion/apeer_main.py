from apeer_dev_kit import adk
import converter


if __name__ == "__main__":
    inputs = adk.get_inputs()

    outputs = converter.execute(inputs['input_image'], inputs['keys'])

    adk.set_file_output('output_image', outputs['output_image'])
    adk.finalize()