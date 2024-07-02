# import yaml
# import os
# current_dir = os.path.dirname(os.path.abspath(__file__))
# project_root = os.path.dirname(current_dir)
# relative_path = "config.yaml"
# yaml_path = os.path.join(project_root, relative_path)

# CONFIG = None


# def reload_config():
#     global CONFIG

#     with open(yaml_path, 'r') as file:
#         CONFIG = yaml.safe_load(file)

#         if CONFIG is None:
#             raise Exception("Config file is empty")


# reload_config()


import os
import yaml

# Obtain the absolute path to the directory where this script is located
current_dir = os.path.dirname(os.path.abspath(__file__))
print("Current Directory:", current_dir)  # Debugging output

# Calculate the path to the project root
project_root = os.path.dirname(current_dir)
print("Project Root:", project_root)  # Debugging output

# Define the path to the YAML file relative to the project root
relative_path = "config.yaml"
yaml_path = os.path.join(project_root, relative_path)
print("YAML Path:", yaml_path)  # Debugging output

CONFIG = None

def reload_config():
    global CONFIG
    with open(yaml_path, 'r') as file:
        CONFIG = yaml.safe_load(file)
    
    if CONFIG is None:
        raise Exception("Config file is empty")

# Call the function to load the configuration
reload_config()
