class Spreadsheet(object):

    def __init__(self, rows):
        """
        :type rows: int
        """
        self.cellValues={}

    def setCell(self, cell, value):
        """
        :type cell: str
        :type value: int
        :rtype: None
        """
        self.cellValues[cell]=value

    def resetCell(self, cell):
        """
        :type cell: str
        :rtype: None
        """
        self.cellValues[cell]=0

    def getValue(self, formula):
        """
        :type formula: str
        :rtype: int
        """
        formula=formula[1:]
        leftop,rightop=formula.split('+')
        def eval(op):
            if op.isdigit():
                return int(op)
            return self.cellValues.get(op,0)
        return eval(leftop)+eval(rightop)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)