import utils.tia_functions as tf
from server import mcp

@mcp.tool()
def open_project(project_path: str, project_name: str) -> str:
    """
    Opens a TIA Portal project given its path and name.

    Args:
        project_path (str): The file path to the TIA Portal project.
                            The default path is "C:\\Users\\{CurrentUser}\\Documents\\Automation".
        
        project_name (str): The name of the TIA Portal project.
    Returns:
        str: A string with the status of the open_project operation.
    """
    return tf.open_project(project_path, project_name)


@mcp.tool()
def close_project() -> str:
    """
    Closes the currently opened TIA Portal project.

    Returns:
        str: A string with the status of the close_project operation.
    """
    return tf.close_project()