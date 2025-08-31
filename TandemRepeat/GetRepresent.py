import sys
from collections import defaultdict

seq_dict = defaultdict(str)
FA_dict = defaultdict(list)

FA = open(sys.argv[1],'r')
for line in FA:
	content = line.strip()
	if content.startswith('>'):
		name = content.strip('>')
	else:
		seq_dict[name] += content
FA.close()

for seq in seq_dict:
	num = 0
	for base in seq_dict[seq]:
		num += 1
		FA_dict[num].append(base)

def get_pos(base_list):

	num1 = num2 = 0
	temp_dict = defaultdict(int)
	for base in base_list:
		num1 += 1
		if base == '-':
			num2 += 1
		else:
			temp_dict[base] += 1
	if num2 / num1 > 0.7:
		return('')
	else:
		best = ''
		best_num = 0
		for base in temp_dict:
			if temp_dict[base] > best_num:
				best = base
				best_num = temp_dict[base]
		return(best.upper())

trf = sys.argv[1].split('/')[-1].split('.')[0]
print('>%s'%trf)
out_line = ''
for pos in range(1,len(FA_dict) + 1):
	out_line += get_pos(FA_dict[pos])
print(out_line + out_line)
