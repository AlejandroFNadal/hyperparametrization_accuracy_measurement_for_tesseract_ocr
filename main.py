# Alejandro Nadal, 2022
import argparse
import pytesseract
import os
from utils.parameters import get_parameters, param_dict_to_string
from utils.logger import printv
from PIL import Image
from unidecode import unidecode

# arguments for command line: input_folder, text_folder, log_file_name (optional), verbose (optional), parameter_file (optional), measure_only (optional)
parser = argparse.ArgumentParser(description='Accuracy measurement and hyperparametrization of tesseract-ocr.')
parser.add_argument('--input_folder', help='Folder containing the images to be processed.')
parser.add_argument('--text_folder', help='Folder containing the text of every image.')
parser.add_argument('--output_folder', help='Folder where the text results will be saved.')
parser.add_argument('--log_file_name', help='Name of the log file.', nargs='?', default='log.txt')
parser.add_argument('-v', '--verbose', help='Prints more information.', action='store_true')
parser.add_argument('-p', '--parameter_file', help='File containing the parameters to be used. Only valid if measure_only', nargs='?', default='parameters.txt')
parser.add_argument('-m', '--measure_only', help='Only measure the accuracy of the images.', action='store_true')
parser.add_argument('--remove-new-line', help='Remove new line characters from the text, converts it into spaces.', action='store_true')
parser.add_argument('--remove-non-ascii', help='Remove non-ascii characters from the text.', action='store_true')
parser.add_argument('--lower-case', help='Convert the text to lower case.', action='store_true')
args = parser.parse_args()



def measure_accuracy(input_folder, text_folder, output_folder, log_file_name, verbose, parameter_file):
    # measure accuracy of the images in input_folder
    # save the results in log_file_name
    # if verbose, print the results to the console
    # return the accuracy of the images
    # list the content of the input_folder. Launch tesseract on each image and save the text in text_folder
    parameters = get_parameters(parameter_file)
    string_parameters = param_dict_to_string(parameters)
    printv('Parameters: ' + param_dict_to_string(parameters), True, verbose)
    printv('Path to input folder: ' + input_folder, True, verbose)
    printv('Path to text folder: ' + text_folder, True, verbose)
    printv('Path to output folder: ' + output_folder, True, verbose)

    input_images = os.listdir(input_folder)
    print(os.path.join(input_folder, input_images[0]))
    # iterate over the images
    for image in input_images:
        # get the text of the image
        binary_image = Image.open(os.path.join(input_folder, image))
        print(binary_image)
        text = pytesseract.image_to_string(binary_image, lang=parameters['lang'])
        if args.remove_new_line:
            text = text.replace('\n', ' ')
        if args.remove_non_ascii:
            text = unidecode(text)
        if args.lower_case:
            text = text.lower()
        # replace extention with txt
        text_file_name = image.split('.')[0] + '.txt'
        # save the text in the text_folder
        with open(os.path.join(output_folder, text_file_name), 'w') as f:
            f.write(text)

if __name__ == '__main__':
    if args.measure_only:
        measure_accuracy(input_folder=args.input_folder, text_folder=args.text_folder, output_folder=args.output_folder, log_file_name=args.log_file_name, verbose=args.verbose, parameter_file=args.parameter_file)