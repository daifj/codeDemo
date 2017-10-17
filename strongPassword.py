import re

def checkPassword(password):
    pwdRegex = re.compile(r'''
        (?=^.{8,}$)       # 八位数及以上
        ((?=.*\d+))       # 至少一位数字
        (?![.\n])         # 没有换行符
        (?=.*[A-Z])       # 大写任意个
        (?=.*[a-z]).*$    # 小写任意个
    ''',re.VERBOSE)

    match = pwdRegex.match(password)
    return match is not None

print('请输入密码：')
password = str(input())
print(checkPassword(password))
