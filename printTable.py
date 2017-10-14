'''表格打印'''

def printTable(tableData):
    # colWidth = [0] * len(tableData)
    maxLen = 0
    # 遍历出最大字符串长度
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            if maxLen < len(tableData[j][i]):
                maxLen = len(tableData[j][i])
            else:
                maxLen
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(maxLen + 1), end='')
        print('')

if __name__ == '__main__':
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    printTable(tableData)