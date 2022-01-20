# Napisz wyrażenie regularne dla LICZB SZESTNASTKOWYCH

# >>> finditer znowu

import re

regex = r"[A-F0-9-]"
test_str = "6F3A 034B 0H21 -342A K534L"

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):

    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))
