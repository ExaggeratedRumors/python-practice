# Napisz wyrażenie regularne dla CZASU w formacie hh:min.sec

import re
regex = r"^([0-1][0-9]:[0-5][0-9].[0-5][0-9])|([2][0-3]:[0-5][0-9].[0-5][0-9])"
test_str = ["23:21.23", "11:59.61", "01:01.01", "25:12.12"]

matches = [re.finditer(regex, string, re.MULTILINE) for string in test_str]

for test in matches:
    for matchNum, match in enumerate(test, start=1):
        print("Match was found: {match}".format(match=match.group()))