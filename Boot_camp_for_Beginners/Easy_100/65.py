s = input()

import re

a = re.compile(r'A.*Z')

k = re.search(a, s)

print(k.end()-k.start())