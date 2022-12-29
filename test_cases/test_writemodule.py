from development.main_module import *
import os


#test case for checking ymal file to flat dict
def test_create_config_file():
    filename = yaml_file_to_flat_dict(os.getcwd()+'\\test\\configurations.txt')
    with open(filename,'r') as fp:
        file_content = fp.readlines()
    output_data = ''
    assert file_content == output_data


#test case for checking cfg or cnf file to flat dict
def test_create_empty_config_file():
    filename = cfg_conf_dict_convertor(os.getcwd()+'\\test\\configurations_test_file.txt')
    with open(filename,'r') as fp:
        file_content = fp.readlines()
    output_data = ['cfs-lib']
    assert file_content == output_data