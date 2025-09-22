from server import mcp
from utils.dice_roll import roll_two_dice

@mcp.tool()
def roll_dice() -> int:
    """
    MCP tool to roll two six-sided dice and return their combined value.
    Returns:
        int: The sum of the two dice rolls.
    """
    return roll_two_dice()