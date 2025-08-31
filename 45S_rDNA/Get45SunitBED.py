import sys
from collections import defaultdict

gff = open(sys.argv[1],'r')
##barrnap output file in GFF format
pos_dict = defaultdict(list)
for line in gff:
	if line.startswith('#'):
		continue
	contents = line.strip().split()
	type_name = contents[8].split(';')[0].split('=')[1]
	if type_name == '18S_rRNA':
		if contents[6] == '+':
			pos_dict[contents[0]].append(int(contents[3]))
		else:
			pos_dict[contents[0]].append(int(contents[4]))
gff.close()

bed_dict = defaultdict(list)
bed = open(sys.argv[2],'r')
##45S.bed
for line in bed:
	contents = line.strip().split()
	bed_dict[contents[0]].append([int(contents[1]),int(contents[2]),contents[3]])
bed.close()

def get_telo(end,pos_list):

	telo = 0
	for pos in pos_list:
		if pos <= end:
			continue
		elif pos - end < 4000:
			telo = pos
		else:
			break
	return(telo)

def get_telo2(start,pos_list):

	telo = 0
	for pos in pos_list:
		if pos < start - 4000:
			continue
		elif start - 4000 <= pos <= start:
			telo = pos
		else:
			break
	return(telo)

out = open('45S_unit.bed','w')
num_dict = defaultdict(int)
for ont in bed_dict:
	if len(bed_dict[ont]) == 1:
		continue
	for term in bed_dict[ont]:
		if term[2] == '+':
			telo = get_telo(term[1],pos_dict[ont])
			if telo != 0:
				num_dict[ont] += 1
				name = '%s_%s'%(ont,num_dict[ont])
				print(ont,term[0] - 1,telo - 1,name,'1',term[2],sep = '\t',file = out)
		elif term[2] == '-':
			telo = get_telo2(term[0],pos_dict[ont])
			if telo != 0:
				num_dict[ont] += 1
				name = '%s_%s'%(ont,num_dict[ont])
				print(ont,telo,term[1],name,'1',term[2],sep = '\t',file = out)
out.close()
