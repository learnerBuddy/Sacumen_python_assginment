
"""
    This module read the .yaml, .cfg, .conf configuration file formats, 
    and generate a flat dictionary out of it. 

    Using flat dictionary it will generate json and env files

    Depending on the requirement, this module write the configurations in .env file, 
    .json file or it should set the configurations in the os environment.
"""


#Libraries
from collections.abc import MutableMapping
from lib2to3.pytree import Base
import os
import sys, configparser, yaml, json


def yaml_file_to_flat_dict(input_file):
    """ Converts a yaml file to flat dictionary."""
    with open(input_file, 'r') as f:
        try:
            """
            safe_load:
                Parse the first YAML document in a stream
                and produce the corresponding Python object.

                Resolve only basic YAML tags. This is known
                to be safe for untrusted input.
            """
            yaml_data = yaml.safe_load(f)
            yaml_flat_dict = flat_dict_convertor(yaml_data)
            return yaml_flat_dict
            f.close()
        except:
            error = "yaml file contains invalid data."
            return error

def cfg_conf_dict_convertor(input_file):
    """ Converts a cfg or a conf file to flat dictionary."""
    try:
        """
        A configuration file consists of sections,
        lead by a "[section]" header,
        and followed by "name: value" entries, with continuations
        """
        config_obj = configparser.ConfigParser()
        config_obj.read(input_file)
        cfg_conf_dict = {}
        for section in config_obj.sections():
            cfg_conf_dict[section] = {}
            for option in config_obj.options(section):
                cfg_conf_dict[section][option] = config_obj.get(section, option)
        cfg_conf_flat_dict = flat_dict_convertor(cfg_conf_dict)
        return cfg_conf_flat_dict
    except:
        error = "cfg or conf file contains invalid input data."
        return error


def flat_dict_convertor(dict_obj: MutableMapping, parent_key: str = '', sep: str ='_'):
    items = []
    for key, value in dict_obj.items():
        new_key = parent_key + sep + key if parent_key else key
        if isinstance(value, MutableMapping):
            items.extend(flat_dict_convertor(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def main():
    """
    main used for Converting cfg, conf, yaml files to flat dictionary
    and save as json, env file. Using input file set the configurations
    in the os environment

    file validations added, if no input provided file throws the error   
    """
    
    try:
        """
           final_list: this is used for collecting error and succes records
           input_files_list: uploaded files stored in this variable
           error_dict: collecting for errors messages
           success_dict: collecting for success messages
        """
        final_list=[]
        error_dict = {}
        success_dict = {}
        input_files_list = []
        configuration_formats_list = []

        print("Supported file formats for the process of set configuration in OS")
        print("1.yaml", "2.cfg", "3.conf")
        file_formats = map(int,input("Please enter file format number with space:").split())
        file_formats = list(file_formats)
        
        print("Please choose output file formats for set the configurations in OS")
        confi_choice = input("By default we are creating json and env files,\nIf you want particluar file format Type Yes/No--[y/n]:")

        if "Yes" in confi_choice or "y" in confi_choice:
            configuration_format = int(input("Please choose file format either 1.json or 2.env:"))
            configuration_formats_list.append(configuration_format)
        else:
            configuration_formats_list.extend([1,2])
        
        try:
            if file_formats[0] and file_formats[1] or file_formats[2]:
                print("Please press enter after entering one file name")
                yaml_file_path = input("Please enter yaml file name here:")
                cfg_conf_file_path = input("Please enter cfg or conf file name here:")
                input_files_list.append(yaml_file_path)
                input_files_list.append(cfg_conf_file_path)
            
        except BaseException:
            if file_formats[0] == 1:
                yaml_file_path = input("Please enter yaml file name here:")
                input_files_list.append(yaml_file_path)
            
            else :
                cfg_conf_file_path = input("Please enter cfg or conf file name here:")
                input_files_list.append(cfg_conf_file_path)
                
        """ Validating and removing none or '' values in files list"""      
        input_files_list = list(filter(None, input_files_list))
        
        for file in input_files_list.copy() :
            
            file_extension = file.split(".")[-1]
            if file_extension=="yaml" or file_extension=="cfg" or file_extension=="conf":
                pass 
            else:
                error = f"{file} not supported.Please upload these formats yaml, cfg, conf files only."
                error_dict[str(file_extension)+"error_file"] = error
                input_files_list.remove(file)
                
        """ Validating and ouput data formats"""
        if 1 or 2 in configuration_formats_list:
            pass
        else:
            del configuration_formats_list
            return f"Supported file formats are .json and .env"
        
        """Generating and setting the configurations in the OS using input files"""
        for index,input_file in enumerate(input_files_list):

            input_file = input_file.strip()
            if os.path.abspath(input_file):
                file_extension = input_file.split(".")[-1]
                
                output_file = None
                if file_extension == 'cfg' or file_extension == 'conf':
                    output_file = cfg_conf_dict_convertor(input_file)
                elif file_extension == 'yaml':
                    output_file = yaml_file_to_flat_dict(input_file)
        
                if "cfg or conf file contains invalid input data." == output_file:
                    error_dict[str(index)]=output_file
                elif "yaml file contains invalid data." == output_file:
                    error_dict[str(index)]=output_file
                    
                else:
                    """generating json and env files"""
                    file_prefix = os.path.splitext(os.path.basename(input_file))[0]
                    
                    if len(configuration_formats_list)==2:
                        output_json_file = file_prefix+"_"+str(index)+ ".json"
                        output_env_file = file_prefix +"_"+str(index)+ ".env"

                        json_obj = json.dumps(output_file, indent=4)
                        with open(output_json_file, "w") as f:
                            f.write(json_obj)
                        f.close()
                        success_dict[str(index)+"json"] = "json files created"
                        
                        try:
                            with open(output_env_file, "w") as f:
                                for key, val in output_file.items():
                                    f.write(f"{key}={val}\n")
                                    os.environ[key] = val
                            f.close()
                            success_dict[str(index)+"env"] = "json files created"
                        except BaseException:
                            error_dict[str(index)+"env"] = "env files not created"
                    else:
                        """generating json or env file based on user input"""
                        config_file_type = configuration_formats_list[0]
                        
                        if config_file_type == 1:
                            output_json_file = file_prefix +"_"+str(index)+ ".json"
                            
                            json_obj = json.dumps(output_file, indent=4)
                            with open(output_json_file, "w") as f:
                                f.write(json_obj)
                            f.close()
                            success_dict[str(index)+"json"] = "json files created"
                            
                        else:
                            try:
                                output_env_file = file_prefix +"_"+str(index)+ ".env"
                                with open(output_env_file, "w") as f:
                                    for key, val in output_file.items():
                                        f.write(f"{key}={val}\n")
                                        os.environ[key] = val
                                f.close()
                                success_dict[str(index)+"env"]= "env files created"
                            except BaseException:
                                error_dict[str(index)+"env"] = "please check uploaded files .env file not created"
            else:
                error_dict[str(input_file)] = "Invalid file Please enter correct file"
                
            """ Sending error and success data to final data"""
            final_list.append(error_dict)
            final_list.append(success_dict)
            
        return final_list
    
    except BaseException:
        return f"Please provide valid data to set the configuration in OS"
        

if(__name__=='__main__'):
    main_function=main()
    sys.exit(main_function)

