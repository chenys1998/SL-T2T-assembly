import sys
from collections import defaultdict

chrom_len = {}
tab = open(sys.argv[1],'r')
for line in tab:
	contents = line.strip().split()
	chrom_len[contents[0]] = int(contents[1])
tab.close()

trgiv_dict = defaultdict(list)
trgiv = open(sys.argv[2],'r')
for line in trgiv:
	contents = line.strip().split()
	trgiv_dict[contents[0]].append([int(contents[3]),int(contents[4])])
trgiv.close()

def get_ratio(start,end,trgiv_list):

	length = 0
	for term in trgiv_list:
		if term[1] < start:
			continue
		elif term[0] <= start <= term[1] <= end:
			length += term[1] - start + 1
		elif start <= term[0] and term[1] <= end:
			length += term[1] - term[0] + 1
		elif start <= term[0] <= end <= term[1]:
			length += end - term[0] + 1
		elif end < term[0]:
			break
	return(round(length / (end - start + 1),4))

for chrom in chrom_len:
	for start in range(0,chrom_len[chrom],100000):
		if start + 100000 > chrom_len[chrom]:
			end = chrom_len[chrom]
		else:
			end = start + 100000
		ratio = get_ratio(start,end,trgiv_dict[chrom])
		print(chrom,start,end,ratio,sep = '\t')
