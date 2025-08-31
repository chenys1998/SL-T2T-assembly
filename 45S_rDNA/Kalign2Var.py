import sys
from collections import defaultdict

seq_list = []
FA_dict = defaultdict(str)
FA = open(sys.argv[1],'r')
for line in FA:
	content = line.strip()
	if content.startswith('>'):
		name = content.strip('>')
		seq_list.append(name)
	else:
		FA_dict[name] += content
FA.close()

length = len(FA_dict[seq_list[0]])

statis_dict = defaultdict(list)
for seq in seq_list:
	index = 0
	print(seq)
	for base in FA_dict[seq]:
		index += 1
		statis_dict[index].append(base)

def caculate(term_list):

	temp_dict = defaultdict(int)
	term_num = 0
	for term in term_list:
		term_num += 1
		temp_dict[term] += 1

	sorted_dict = dict(sorted(temp_dict.items(),key = lambda x:x[1],reverse = True))
	key_list = []
	value_list = []
	value2_list = []
	for key in sorted_dict:
		key_list.append(key)
		value2_list.append(str(sorted_dict[key]))
		value_list.append(str(round(sorted_dict[key] / term_num,2)))
	key_str = '/'.join(key_list)
	value_str = '/'.join(value_list)
	value2_str = '/'.join(value2_list)
	return(key_str,value_str,value2_str)

out = open(sys.argv[2],'w')
print('#Pos','Var','Ratio',sep = '\t',file = out)
for index in range(1,length + 1):
	key_str,value_str,value2_str = caculate(statis_dict[index])
	print(index,key_str,value_str,value2_str,sep = '\t',file = out)
out.close()
