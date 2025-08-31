import sys
from collections import defaultdict

def get_num(fafile):

	num = 0
	fa = open(fafile,'r')
	for line in fa:
		content = line.strip()
		if content.startswith('>'):
			num += 1
	return(num)

len_dict = defaultdict(int)
num_dict = defaultdict(int)
tab = open(sys.argv[1],'r')
for line in tab:
	content = line.strip()
	if content.startswith('>'):
		name = content.strip('>')
		num_dict[name] = get_num('%s/%s.fa'%(sys.argv[2],name))
	else:
		len_dict[name] += len(content)
tab.close()

for term in len_dict:
	print(term,len_dict[term],num_dict[term],sep = '\t')
