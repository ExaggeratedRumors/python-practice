# Napisz wyrażenie regularne dla TABLIC REJESTRACYJNYCH
import re
regex = r"^([A-Z]{1,3} [0-9A-Z]{3,5})"
test_str = ["ELC 5454", "WA 1235", "2WA 54WA", "54A PGFADF"]

matches = [re.finditer(regex, string, re.MULTILINE) for string in test_str]

for test in matches:
    for matchNum, match in enumerate(test, start=1):
        print("Match was found: {match}".format(match=match.group()))
