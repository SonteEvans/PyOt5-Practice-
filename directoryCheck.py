import os

def check_and_create_directory():
    directory = os.path.join("C:", "Shotgun") if os.name == 'nt' else os.path.join(os.path.expanduser("~"), "Shotgun")

    if not os.path.exists(directory):
        os.makedirs(directory)
        return f"Directory '{directory}' created."
    else:
        return f"Directory '{directory}' already exists."