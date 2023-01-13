import re

pattern = "^python"
replaceWord = "Java"
samples = ["pythonあいうえお", "かきくけこ", "さしすせそpython"]

for sample in samples:
    if re.findall(pattern, sample):
        print(re.sub(pattern, replaceWord, sample))
