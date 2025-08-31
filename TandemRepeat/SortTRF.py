import sys
from collections import defaultdict

length_dict = defaultdict(list)
gff = open(sys.argv[1],'r')
for line in gff:
	contents = line.strip().split()
	name = contents[8].split(';')[0].split('=')[1]
	if int(contents[4]) > int(contents[3]):
		length_dict[name].append([int(contents[3]),int(contents[4])])
	else:
		length_dict[name].append([int(contents[4]),int(contents[3])])
gff.close()

def get_len(length_list):

	length = 0
	temp_list = []
	temp_dict = {}
	for term in length_list:
		if term[0] not in temp_list:
			temp_list.append(term[0])
			temp_dict[term[0]] = term[1]
		elif temp_dict[term[0]] < term[1]:
			temp_dict[term[0]] = term[1]
	temp_list.sort()

	working_list = []
	for index in temp_list:
		if working_list == []:
			working_list = [index,temp_dict[index]]
		elif working_list[1] < index:
			length += working_list[1] - working_list[0] + 1
			working_list = [index,temp_dict[index]]
		elif index <= working_list[1] < temp_dict[index]:
			working_list[1] = temp_dict[index]
	length += working_list[1] - working_list[0] + 1
	return(length)

result_dict = defaultdict(int)
for term in length_dict:
	trf = term.split('@')[1]
	result_dict[trf] += get_len(length_dict[term])

for trf in result_dict:
	print(trf,result_dict[trf],sep = '\t')
