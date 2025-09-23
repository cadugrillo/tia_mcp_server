import json
import tia_portal.config as tia_config
from tia_portal import Client, Project

openned_project = None
openned_project_path = ""
openned_project_name = ""


def open_project(project_path: str, project_name: str) -> str:
    """
    Opens a TIA Portal project located at the specified path.

    Args:
        project_path (str): The file path to the TIA Portal project.
                            The default path is "C:\\Users\\{CurrentUser}\\Documents\\Automation".
        
        project_name (str): The name of the TIA Portal project.

    Returns:
        str: A string with the status of the open_project operation.
    """
    global openned_project, openned_project_path, openned_project_name

    tia_config.load()
    tia_client = Client()
    
    if openned_project is not None:
        return "A project is already opened. Please close it before opening another one."

    # Try open the project at the given path
    try:
        openned_project = tia_client.open_project(project_path, project_name)
    except Exception as e:
        # openned_project = None
        return f"Failed to open project: {e}"
    else:
        openned_project_path = project_path
        openned_project_name = project_name
        return f"Project '{project_name}' at '{project_path}'opened successfully."


def close_project() -> str:
    """
    Closes the currently opened TIA Portal project.
    Returns:
        str: A string with the status of the close_project operation.
    """
    global openned_project

    if openned_project is not None:
        openned_project.close()
        openned_project = None
        return "Project closed successfully."
    else:
        return "No project is currently opened."
    

def save_project() -> str:
    """
    Saves the currently opened TIA Portal project.
    Returns:
        str: A string with the status of the save_project operation.
    """
    global openned_project

    if openned_project is not None:
        openned_project.save()
        return "Project saved successfully."
    else:
        return "No project is currently opened."


def save_project_as(project: Project, new_name: str) -> str:
    """
    Saves the currently opened TIA Portal project under a new name and path.

    Args:
        new_name (str): The new name for the project.
    Returns:
        str: A string with the status of the save_project_as operation.
    """
    global openned_project

    if openned_project is not None:
        openned_project.save_as(new_name)
        return "Project renamed successfully."
    else:
        return "No project is currently opened."


def add_plc(article_no: str, version: str, device_name: str) -> str:
    """
    Adds a PLC to the currently opened TIA Portal project.

    Args:
        article_no (str): The article number, also known as MLFB (Maschinen-Liefer-Fertigungs-Nummer), of the PLC to add.
        version (str): The version of the PLC to add.
        device_name (str): The name of the device to add.
    Returns:
        str: A string with the status of the add_device operation.
    """
    global openned_project

    if openned_project is not None:
        try:
            openned_project.devices.create_PLC(article_no, version, device_name, device_name)
        except Exception as e:
            return f"Failed to add PLC: {e}"
        else:
            return f"PLC '{device_name}' added successfully."
    else:
        return "No project is currently opened."
    

def get_plcs() -> str:
    """
    Retrieves a list of PLCs in the currently opened TIA Portal project.

    Returns:
        list: A list of PLC indexes and names in the project.
    """
    global openned_project

    if openned_project is not None:
        try:
            plcs = openned_project.get_plcs()
        except Exception as e:
            return f"Failed to get PLCs: {e}"
        else:
            plc_list = []
            for i in range(len(plcs)):
                plc_list.append({
                    "index": i,
                    "name": plcs[i].name,
                })
            return f"PLC(s) found in project: {plc_list}"
    else:
        return "No project is currently opened."
    

def get_plc_blocks(index: int) -> str:
    """
    Retrieves the blocks details of a PLC in the currently opened TIA Portal project by its index.

    Args:
        index (int): The index of the PLC in the project (0-based).

    Returns:
        str: A string containing details of the PLC blocks.
    """

    global openned_project

    if openned_project is not None:
        try:
            blocks = openned_project.get_plcs()[index].get_software().get_all_blocks(recursive=True)  
        except Exception as e:
            return f"Failed to get PLC Blocks: {e}"
        else:
            block_list = []
            for i in range(len(blocks)):
                block_list.append({
                    "index": i,
                    "name": blocks[i].name if blocks[i].name else "Unknown",
                    "type": blocks[i].get_type()
                })
            return f"PLC Index {index} Block List: {block_list}"
    else:
        return "No project is currently opened."