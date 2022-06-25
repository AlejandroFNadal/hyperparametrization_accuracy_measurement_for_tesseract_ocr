import os

valid_parameters = ['psm', 'oem', 'lang']
def get_parameters(parameter_file):
    # get the parameters from the parameter_file
    # return the parameters
    with open(parameter_file, 'r') as f:
        lines = f.read().splitlines()
        parameters = {}
        for line in lines:
            key, value = line.split('=')
            parameters[key] = value
    return parameters

def param_dict_to_string(params):
    return f"--psm {params['psm']} --oem {params['oem']}"