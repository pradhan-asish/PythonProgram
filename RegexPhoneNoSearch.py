import re

phoneRegex = re.compile ( r'''
(((\d\d\d)|(\(\d\d\d\)))? #area code
(-|\s) # first separator
\d\d\d # first 3 digits
-      # separator
\d\d\d\d # last 4 digits
(((ext(\.)?\s)|x) # extension word-part (Optional)
(\d{2,5}))?)       # extension number-part (Optional)
''', re.VERBOSE)


text = '123-321-1234 , 987-852-7895'
phoneNums = phoneRegex.findall(text)
phoneList = []

for phone in phoneNums:
    phoneList.append(phone[0])

print(phoneList)
