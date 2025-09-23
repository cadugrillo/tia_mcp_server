import utils.tia_functions as tf
from server import mcp

@mcp.tool()
def get_plc_blocks(index: int) -> str:
    """
    Retrieves the blocks details of a PLC in the currently opened TIA Portal project by its index.

    Args:
        index (int): The index of the PLC in the project (0-based).

    Returns:
        str: A string containing details of the PLC blocks.
    """
    return tf.get_plc_blocks(index)