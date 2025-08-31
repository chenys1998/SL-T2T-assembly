import sys
from collections import defaultdict

result_dict = defaultdict(list)
tab = open(sys.argv[1],'r')
for line in tab:
	contents = line.strip().split()
	if float(contents[2]) >= 90 and int(contents[3]) >= 500:
		if int(contents[9]) > int(contents[8]):
			result_dict[contents[1]].append([int(contents[8]),int(contents[9])])
		else:
			result_dict[contents[1]].append([int(contents[9]),int(contents[8])])
tab.close()

for chrom in result_dict:
	temp_list = []
	temp_dict = {}
	for target in result_dict[chrom]:
		if target[0] not in temp_list:
			temp_list.append(target[0])
			temp_dict[target[0]] = target[1]
		elif temp_dict[target[0]] < target[1]:
			temp_dict[target[0]] = target[1]
	temp_list.sort()
	working_list = []
	for index in temp_list:
		if working_list == []:
			working_list = [index,temp_dict[index]]
		elif working_list[1] < index:
			print(chrom,'-','-',working_list[0],working_list[1],sep = '\t')
			working_list = [index,temp_dict[index]]
		elif index <= working_list[1] <= temp_dict[index]:
			working_list[1] = temp_dict[index]
	print(chrom,'-','-',working_list[0],working_list[1],sep = '\t')
