def reverse(strList, start, end):
    while start < end:
        strList[start], strList[end] = strList[end], strList[start]
        start += 1
        end -= 1
str = 'I love China!'
strList = list(str)
i = 0
while i < len(strList):
    if strList[i] != ' ':
        start = i
        end = start + 1
        while (end < len(strList)) and strList[end] != ' ':
            end += 1
        reverse(strList, start, end - 1)
        i = end
    else:
        i += 1
strList.reverse()
print(''.join(strList))
