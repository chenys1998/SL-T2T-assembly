import sys
from collections import defaultdict

ont_list = []
s58_dict = defaultdict(list)
s18_dict = defaultdict(list)
s28_dict = defaultdict(list)
front_dict = defaultdict(int)
back_dict = defaultdict(int)
working = ''
gff = open(sys.argv[1],'r')
##barrnap output file in GFF format
for line in gff:
	contents = line.strip().split('\t')
	if line.startswith('#'):
		continue
	if contents[0] not in ont_list:
		ont_list.append(contents[0])
	name = contents[8].split(';')[0].split('=')[1]
	if name not in ['5_8S_rRNA','18S_rRNA','28S_rRNA'] or len(contents[8].split(';')) > 2:
		continue
	rdna_term = contents[8].split(';')[0].split('=')[1]
	if contents[6] == '+':
		front_dict[contents[0]] += 1
	else:
		back_dict[contents[0]] += 1
	if rdna_term == '5_8S_rRNA':
		s58_dict[contents[0]].append([int(contents[3]),int(contents[4])])
	elif rdna_term == '18S_rRNA':
		s18_dict[contents[0]].append([int(contents[3]),int(contents[4])])
	elif rdna_term == '28S_rRNA':
		s28_dict[contents[0]].append([int(contents[3]),int(contents[4])])
gff.close()

def test128(end,s128_list):

	state = []
	for term in s128_list:
		if term[0] < end:
			continue
		elif term[0] <= end + 500:
			state = term
			break
		else:
			break
	return(state)

def test58(start,end,s58_list):

	state = 0
	for term in s58_list:
		if term[1] < start:
			continue
		elif start <= term[0] and term[1] <= end:
			state = 1
			break
		else:
			break
	return(state)
			

def get_rdna1(s58_list,s18_list,s28_list):

	result_list = []
	for term in s18_list:
		test = test128(term[1],s28_list)
		if test != [] and test58(test[0],test[1],s58_list):
			result_list.append([term[0],test[1]])
	return(result_list)

def get_rdna2(s58_list,s18_list,s28_list):
	result_list = []
	for term in s28_list:
		test = test128(term[1],s18_list)
		if test != [] and test58(term[0],term[1],s58_list):
			result_list.append([term[0],test[1]])
	return(result_list)

def add_len(rdna_list):

	length = 0
	for term in rdna_list:
		length += term[1] - term[0] + 1
	return(length)

out = open('45s.bed','w')
for ont in ont_list:
	if ont not in s58_dict:
		continue
	if front_dict[ont] > back_dict[ont]:
		result_list = get_rdna1(s58_dict[ont],s18_dict[ont],s28_dict[ont])
		if result_list != []:
			length = add_len(result_list)
			if length > 5000:
				for term in result_list:
					print(ont,term[0],term[1],'+',sep = '\t',file = out)
	else:
		result_list = get_rdna2(s58_dict[ont],s18_dict[ont],s28_dict[ont])
		if result_list != []:
			length = add_len(result_list)
			if length > 5000:
				for term in result_list:
					print(ont,term[0],term[1],'-',sep = '\t',file = out)
tab.close()
