import sys,os
from collections import defaultdict

fa_dict = defaultdict(str)
fa = open(sys.argv[2],'r')
for line in fa:
	content = line.strip()
	if line.startswith('>'):
		name = content.strip('>')
	else:
		fa_dict[name] += content
fa.close()

final_dict = defaultdict(dict)
tab_list = os.popen('ls %s/*.tab'%sys.argv[1],'r')
for tab_file in tab_list.read().split():
	seq_name = tab_file.split('/')[-1].split('.')[0]
	print(seq_name)
	seq_dict = defaultdict(dict)
	tab = open(tab_file,'r')
	for line in tab:
		contents = line.strip().split()
		bases = contents[2].split('/')
		nums = contents[4].split('/')
		for index in range(len(bases)):
			seq_dict[int(contents[0])][bases[index]] = int(nums[index])
	tab.close()

	pre_index = index = 0
	for base in fa_dict[seq_name]:
		index += 1
		if base == '-':
			continue
		pre_index += 1

		for target in seq_dict[pre_index]:
			if target not in final_dict[index]:
				final_dict[index][target] = seq_dict[pre_index][target]
			else:
				final_dict[index][target] += seq_dict[pre_index][target]
tab_list.close()

def sort_term(temp_dict):

	sorted_dict = dict(sorted(temp_dict.items(),key = lambda x:x[1],reverse = True))
	key_list = []
	value_list = []
	value2_list = []
	SUM = sum(sorted_dict.values())
	for term in sorted_dict:
		key_list.append(term)
		value_list.append(str(sorted_dict[term]))
		value2_list.append(str(round(sorted_dict[term] / SUM,2)))
	return('/'.join(key_list),'/'.join(value_list),'/'.join(value2_list))

length = len(final_dict)
out = open(sys.argv[3],'w')
for i in range(1,length + 1):
	key_str,value_str,value2_str = sort_term(final_dict[i])
	print(i,key_str,value_str,value2_str,sep = '\t',file = out)
out.close()
