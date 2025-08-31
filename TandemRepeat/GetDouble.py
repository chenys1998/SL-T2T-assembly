import sys
from collections import defaultdict

seq_dict = defaultdict(str)
fa = open(sys.argv[1],'r')
for line in fa:
	content = line.strip()
	if content.startswith('>'):
		name = content.strip('>')
	else:
		seq_dict[name] += content
fa.close()

for seq in seq_dict:
	print('>%s'%seq)
	print(seq_dict[seq] + seq_dict[seq])
