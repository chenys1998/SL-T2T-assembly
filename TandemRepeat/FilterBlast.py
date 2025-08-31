import sys
from collections import defaultdict

seq_list = []
order_dict = {}
num_dict = {}
length_dict = {}

line_num = 0
tab = open(sys.argv[1],'r')
for line in tab:
	line_num += 1
	contents = line.strip().split()
	seq_list.append(contents[0])
	order_dict[contents[0]] = line_num
	num_dict[contents[0]] = int(contents[2])
	length_dict[contents[0]] = int(contents[1]) / 2
tab.close()

done_list = []
done_dict = defaultdict(list)
target_dict = defaultdict(list)
blast = open(sys.argv[2],'r')
for line in blast:
	contents = line.strip().split()
	if contents[0] == contents[1] or order_dict[contents[0]] < order_dict[contents[1]]:
		continue
	if float(contents[2]) >= 90 and int(contents[3]) / length_dict[contents[0]] >= 0.9:
		if contents[0] not in done_list:
			done_list.append(contents[0])
		done_dict[contents[1]].append(contents[0])
		if int(contents[3]) / length_dict[contents[1]] >= 0.9 and num_dict[contents[0]] > num_dict[contents[1]]:
			target_dict[contents[1]].append(contents[0])
blast.close()

result_dict = defaultdict(list)
for seq in seq_list:
	if seq in done_list:
		continue
	elif len(target_dict[seq]) == 0:
		result_dict[seq] = [seq] + done_dict[seq]
	else:
		best = ''
		best_num = 0
		for target in target_dict[seq]:
			if num_dict[target] > best_num:
				best = target
				best_num = num_dict[target]
		if seq not in result_dict[best]:
			result_dict[best].append(seq)
		for term in done_dict[seq]:
			if term not in result_dict[best]:
				result_dict[best].append(term)

for result in result_dict:
	print(result,len(result_dict[result]),';'.join(result_dict[result]),sep = '\t')	
