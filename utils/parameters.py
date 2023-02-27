import os
parameter_grid = {
    'psm':{
        'min': 1,
        'max': 13,
        'step': 1,
        'curr': 1
    },
    'oem':{
        'min': 0,
        'max': 3,
        'step' :1,
        'curr': 0
    }
}
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

def main_args_checker(args):
    #this includes the logic check of arguments of the main function
    #return True if the arguments are valid, False otherwise
    if args.parameter_file and (not args.measure_only):
        print('Error: --parameter_file can only be used with --measure_only')
        return False
    return True

 