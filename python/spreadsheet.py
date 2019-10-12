
class SpreadSheet:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.sheet = [[None] * cols] * rows

    def updateCell(self, i, j, val):
        self.sheet[i][j] = val
        # self.printSheet()

    # def printSheet(self):
    #     for i in range(len(self.sheet)):
    #         string = ""
    #         for j in range(len(self.sheet[i])):
    #             if j == len(self.sheet[i]) - 1:
    #                 string += str(self.sheet[i][j])
    #             else:
    #                 string += str(self.sheet[i][j]) + "|"
    #         print(string)



sheet = SpreadSheet(4, 3)
# print(sheet.sheet)
sheet.updateCell(0, 0, "bob")
# sheet.updateCell(1, 0, "alice")
print(sheet.sheet)
# print(sheet.sheet[1])
# row1 = ["bob", 10, "foo"]
# # row2 = ["alice", 5]
#
# for i in range(len(row1)):
#     sheet.updateCell(0, i, row1[i])
#
# for i in range(len(row2)):
#     sheet.updateCell(1, i, row1[i])
