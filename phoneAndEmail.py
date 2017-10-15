import pyperclip, re

phoneRegex = re.compile(r'([1][3-9]\d{9})')

# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+  # username
    @
    [a-zA-Z0-9.-]+     # domain name
    (\.[a-zA-Z]{2,4})  # dot-something
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    matches.append(groups)
for groups in  emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone number or email addresses found.')
