import sys
from collections import defaultdict

all_dict = defaultdict(int)
fa = open(sys.argv[1],'r')
for line in fa:
	content = line.strip()
	if content.startswith('>'):
		chrom = content.lstrip('>').split()[0]
	else:
		all_dict[chrom] += len(content)
fa.close()

for i in all_dict:
	print(i,all_dict[i],sep = '\t')
