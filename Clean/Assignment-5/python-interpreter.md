# Python Interpreter
If you are able to run the existing code of the project you can skip these instructions.
This tutorial shows you how to configure a Python interpreter for your project.

## Adding a Python Interpreter to a Project

1. For Windows and Linux: Click on `File` -> `Settings`.

   For MacOs: Click on `PyCharm` -> `Preferences...`.

2. Navigate in the menu to `Project` and click on `Python Interpreter`.

3. Click the gear (at the top right corner) and then click on`Add`.

4. Select `Conda Environment` and select `Python version 3.7` (depends on your python installation)

   The execution path should look like this for Windows and Linux: 

   *C:\Users\username\anaconda3\Scripts\conda.exe*

   And like this for MacOs: 

   */home/opt/anaconda3/bin/conda*

5. Click `OK` to create the environment.

6. Make sure this new environment is selected as your Python Interpreter and click `OK`.


## Run the Python Project

There are two ways you can run the project:

#### First Option

1. Navigate to the `__main__.py` in the project overview on the right.

2. Right click on `__main__.py`.

3. Click on `Run '__main__'`. The following window will be displayed, and you can interact with the program.

#### Second Option

1. Click on the `Terminal` panel of the editor.

2. Type the following command in Windows and Linux `python -m books.__main__`, and in MacOs `pythonw -m books.__main__`, to run the Python project. The `-m` option stands for module. You need to point to a valid absolute Python module name. This command will display the Graphical User Interface (GUI) to interact with the program.






