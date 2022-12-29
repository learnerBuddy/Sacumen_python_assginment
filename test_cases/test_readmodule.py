from development.main_module import *
import os

#test case for checking ymal file to flat dict
def test_convert_yaml_file():
    input_file = "file.yaml"
    expected_output = {'languages:': {'  pascal': 'Lame', '  python': 'Elite', '  perl': 'Elite'}, 'foods:': ['Mango', 'Strawberry', 'Orange', 'Apple'], 'employed': 'True', 'skill': 'Elite', 'job': 'Developer', 'name': "Martin D'vloper"}
    assert yaml_file_to_flat_dict(os.getcwd()+'\\test\\test.yaml') == expected_output

#test case for checking cfg or cnf file to flat dict
def test_convert_conf_cfg_file():
    expected_output = {'section1': {'database': 'database1', 'server': 'server2', 'host': 'host2', 'port': '798'}, 'cfs-lib': {'server': 'server1', 'host': 'host1', 'port': '6776'}}
    assert cfg_conf_dict_convertor(os.getcwd()+'\\test\\test.conf') == expected_output

 