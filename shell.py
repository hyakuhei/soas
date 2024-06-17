import logging, datetime, os, importlib.util, json

import pprint

from colors import color #requires ansicolors

from consolemenu import *
from consolemenu.items import *

pp = pprint.PrettyPrinter(indent=4)

timestr = datetime.datetime.now().strftime('%d-%m-%y-%H-%M-%S')
logger = logging.basicConfig(filename=f"{__name__}-{timestr}", encoding='utf-8', level=logging.DEBUG)
logging.info(timestr)

logging.info(os.environ)

# Script Target Folder
# Replace this later with a shell configuration file
SCRIPTS="scripts"

def _gatherScripts():
    from os import listdir
    from os.path import isfile, join
    scripts = [f for f in listdir(SCRIPTS) if (isfile(join(SCRIPTS,f)) and f.endswith('.py'))]
    scripts.remove('__init__.py')
    scripts = [s.split(".py")[0] for s in scripts] #trim away the '.py'

    loaded_scripts = {}

    for script in scripts:

        spec = importlib.util.spec_from_file_location(script, f"{SCRIPTS}/{script}.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
  
        loaded_scripts[script] = module

    return loaded_scripts

def _run(action):
    x = action()
    #print(json.dumps(x))
    pp.pprint(x)
    PromptUtils(Screen()).enter_to_continue()

def main():
    menu = ConsoleMenu("Safe Operator Access Shell", "Activities are logged. Seek permission to go 'off script'")
    
    loaded_modules = _gatherScripts()

    for m in loaded_modules.keys():
        declaration = loaded_modules[m].declaration()
        
        # Override color
        t = color(f"{declaration['name']}", fg="blue")
        if declaration['behaviors']["mutating"] == True: t = color(f"{declaration['name']}", fg="yellow")
        if declaration['behaviors']['dangerous'] == True: t = color(f"{declaration['name']}", fg="red")

        menu.append_item(
            FunctionItem(
                t,
                _run,
                args=[loaded_modules[m].entrypoint])
            )
        # print(f"{m} : {loaded_modules[m].declaration()}")
    
    menu.append_item(
        CommandItem(
            color('Run a console command', fg="purple"),
            "/bin/.sh"
        )
    )
    menu.start()
    menu.join()

if __name__ == '__main__':
    main()
else:
    raise Exception("Do not include shell.py")