import utils.tia_functions as tf
from server import mcp

@mcp.tool()
def add_plc(article_no: str, version: str, device_name: str) -> str:
    """
    Adds a new PLC to the currently opened TIA Portal project.

    Args:
        article_no (str): The article number of the PLC to be added.
        version (str): The version of the PLC to be added.
        device_name (str): The name to assign to the new PLC device in the project.

    Returns:
        str: A string with the status of the add_plc operation.
    """
    return tf.add_plc(article_no, version, device_name)

@mcp.tool()
def get_plcs() -> list:
    """
    Retrieves a list of PLCs in the currently opened TIA Portal project.

    Returns:
        list: A list of dictionaries, each containing details of a PLC in the project.
    """
    return tf.get_plcs()