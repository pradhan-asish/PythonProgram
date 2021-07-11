import re

emailRegex = re.compile('''
[A-za-z0-9+_.]+ ## Before @ part
\@
[A-za-z0-9+_]+ ## Before .domai part
[.A-za-z]+  ## Domain Part
''',re.VERBOSE)

text = 'pradhan.asish1994@gamil.com sburris@comcast.net rgriffin45@optonline.net'

mailAddress = emailRegex.findall(text)
print(mailAddress)
