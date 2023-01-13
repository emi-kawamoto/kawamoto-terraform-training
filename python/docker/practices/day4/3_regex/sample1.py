import re

pattern = "^python"
samples = ["pythonあいうえお", "かきくけこ", "さしすせそpython"]

for sample in samples:
    if re.findall(pattern, sample):
        print(sample)
