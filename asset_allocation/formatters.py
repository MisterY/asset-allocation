"""
Output formatters for the AA model
"""
from .model import AssetAllocationModel, AssetClass


class AsciiFormatter:
    """ Formats the model for the console output """
    # def __init__(self):
    #     super.__init__(self)

    def format(self, model: AssetAllocationModel):
        """ Returns the view-friendly output of the aa model """
        output = "AA model\n"
        output += "Total amount: " + str(model.total_amount) + "\n"
        # Asset classes
        output += "Asset Allocation\n"
        for ac in model.classes:
            output += self.__get_ac_tree(ac)
        return output

    def __get_ac_tree(self, ac: AssetClass):
        """ formats the ac tree - entity with child elements """
        output = self.__get_ac_row(ac) + "\n"
        for child in ac.classes:
            output += self.__get_ac_tree(child)
        return output

    def __get_ac_row(self, ac: AssetClass):
        """ Formats one Asset Class record """
        output = ""
        # Indent according to depth.
        for _ in range(0, ac.depth):
            output = f"    {output}"
        
        output += f"{ac.name: <25}: "
        
        allocation = f"{ac.allocation:.2f}"
        output += f"{allocation:>5}"
        return output

class HtmlFormatter:
    """ Formats HTML output """
    pass
    