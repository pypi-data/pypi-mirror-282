if __name__ == "__main__":
    import sys
    sys.path.append("/home/erwan/eve/test/asm/src")
import asmat.generation as generation
import asmat.dependencies as files
import asmat.const as const
import os
import asmat.validation as validation
from asmat.analysis.analyze import analyze

"""
        Assembly Analysis and Testing

This is the main file of the ASMAT.
ASMAT is originally made for validating EVE assembly code.
The scope of this module has increase to be used on other c++ libraries.

The 3 main usefulness of this module are:
    - generation
    - validation
    - analysis
"""



def flags_to_command_line(flags:list):
    fl = []
    for i in flags:
        fl.append('-' + i)
    return fl



def options_to_dict(options:list):
    """Get dictionary from args list

    Args:
        options (list): List of options given by os.argv. The first element of the list should be the name of the file.

    Raises:
        Exception: If option `-input` is not followed by files names
        Exception: If the option doesn't exist

    Returns:
       dict : dictionary with each option value
    """
    opt = const.OPTIONS.copy()

    i = 1
    while i < len(options):
        if options[i] == '-m':
            lst = []
            while i+1 < len(options) and options[i+1][0] != '-':
                lst.append(options[i+1])
                i+=1
            if len(lst) == 0:
                raise Exception("Parameter missing for option -m")
            for j in lst:
                if j not in const.ARCH:
                    raise Exception(f"Invalid architecture name '{j}'")
            opt['arch'] = lst
        elif options[i] == '-l':
            opt['log'] = True
        elif options[i] == "-d":
            opt['deep'] = True
        elif options[i] == "-a" or options[i] == "--analysis":
            opt['analyze'] = True
            opt['validate'] = False
            opt['generate'] = False
        elif options[i] == '-t':
            opt['keep_tmp'] = True
        elif options[i] == '-g':
            opt['generate'] = True
            opt['validate'] = False
            opt['analyze'] = False
        elif options[i] == '-i':
            opt["instruction_comparison"] = True
        elif options[i] == '-v':
            opt['verbose'] = True
        elif options[i] == "--version":
            print(const.VERSION)
            opt['validate'] = False
            opt['generate'] = False
            opt['analyze'] = False
        elif options[i] == '--fatal':
            opt['exception'] = True
        elif options[i] == '--functionsperfile' or options[i] == '-S':
            opt['limit_per_file'] = int(options[i+1])
            i+=1
        elif options[i] == '--ref':
            opt['ref_path'] = options[i+1]
            i+=1
        elif options[i] == '--reset':
            opt['validate'] = False
            opt['generate'] = False
            opt['analyze'] = False
            e = input("All references files will be deleted, do you confirm ? (Y/n)")
            if e == 'Y':
                files.reset()
            break
        elif options[i] == '--build':
            opt['validate'] = False
            opt['generate'] = False
            opt['analyze'] = False
            files.build_dependencies()
            break
        elif options[i] == "--disassembler" or options[i] == "-D":
            if options[i+1] == 'objdump' or options[i+1] == 'standard':
                opt['disassembler'] = options[i+1]
                i+=1
            else:
                raise Exception("Invalid parameter with option disassembler. Valid parameters are `standard` or `objdump`")
        elif options[i] == '--input':
            if options[i+1][0] == '-':
                raise Exception("Invalid parameter for option --input")
            opt['input'] = options[i+1]
            i+=1
        elif options[i] == '--flags':
            lst = []
            while i+1 < len(options) and options[i+1][0] != '-':
                lst.append('-' + options[i+1])
                i+=1
            if len(lst) == 0:
                raise Exception("Parameter missing for option --output")
            opt['flags'] = lst
        elif options[i] == '--output':
            opt['output'] = options[i+1]
            i+=1
        elif options[i] == '--setup' or options[i] == '-s':
            opt['setup'] = options[i+1]
            i+=1
        elif options[i] == '--settings':
            s = options[i+1]
            if os.path.exists(f"{const.root}/{s}"):
                if os.path.isdir(f"{const.root}/{s}"):
                    opt['settings'] = [f"{const.root}/{s}/{i}" for i in os.listdir(f"{const.root}/{s}")]
                else:
                    opt['settings'] = [f"{const.root}/{s}"]
            elif os.path.exists(s):
                opt['settings'] = [s]
            else:
                raise Exception("Invalid settings path")
            i += 1
            
        elif options[i] == '--compiler' or options[i] == '-c':
            opt['compiler'] = options[i+1]
            i+=1
        elif options[i] == '-j':
            opt['nbprocess'] = int(options[i+1])
            i+=1

        elif options[i] == '--header' or options[i] == '-H':
            lst = []
            while i+1 < len(options) and options[i+1][0] != '-':
                lst.append(options[i+1])
                i+=1
            if len(lst) == 0:
                raise Exception("Parameter missing for option --header")
            opt['headers'] = lst

        else:
            raise Exception(f"Invalid option {options[i]}")
        i+=1

    return opt



def main(opt):

    if opt['generate']:
        return generation.generate(opt, opt['limit_per_file'])
    elif opt['validate']:
        return validation.validate(opt, opt['limit_per_file'])
    elif opt['analyze']:
        return analyze(opt, opt['compiler'], opt['setup'])



def run():
    argv = sys.argv
    
    options = options_to_dict(argv)
    return main(options)

if __name__ == '__main__':
    run()