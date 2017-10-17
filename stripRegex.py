import re

def strip(text, chars = None):
    '''去除首尾的字符

    :type text: string
    :type chars: string
    :rtype: string
    '''
    if chars is None:
        reg = re.compile('^ *| *$')
    else:
        reg = re.compile('[' + chars + ']*')
    return reg.sub('', text)

print(strip('  asffa  '))
print(strip(' 122456  45422 ', '2'))
print(strip('afaflge mkldafa', 'al'))
