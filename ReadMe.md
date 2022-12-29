### Details about Module 
This Project is designed to create a module which can read .yaml, .cfg and .conf file formats
   and generate a flat dictionary out of it.

Depending upon the user inputs given, module should store the configurations in .env or .json file format or set the configurations in os environment.
1. Requirements to install virtual env:
    `pip install virtualenv` /* Install virtual environment */
    `virtualenv venv`  /* Create a virtual environment */
    `venv/bin/activate` /* Activate the virtual environment */
    
    For Windows System:
    `https://programwithus.com/learn/python/pip-virtualenv-windows`
    
2. Requirements to install
    'install python version if using windows' 
    `url:https://www.python.org/downloads/`
    `pip install pyyaml`

3. Install pytest module for creating unit test cases
    `pip install pytest`

4. Before creating wheel file, we need to install python packages
    `pip install wheel setuptools`

#-- if `python` command not work try running file using `python3` 

5. Generate wheel file
    `python setup.py bdist_wheel`

6. A dist folder gets created which stores the wheel(.whl) file.

7. Run pip install < wheel file name > 

####To start the functionality run the py file plese follow below mentioned steps:

1.Switch to development directory Run python file:
    `python main_module.py` or `python3 main_module.py `
    
2.please `follow the steps` after executing file.

3.Enter File names of `yaml, cfg, conf`.

4.Enter ouput format for seeting `OS configuration`

5.Generated files are avilable in `development folder`.

6.Test cases are written in `test_cases` folder
 
