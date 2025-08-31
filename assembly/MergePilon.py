import sys,os
from collections import defaultdict

def read_fa(fafile):

	seq = ''
	with open(fafile,'r') as fa:
		for line in fa:
			content = line.strip()
			if content.startswith('>'):
				continue
			seq += content
	return(seq)

index_dict = defaultdict(int)
seq_dict = {}
fa_list = os.popen('ls %s/*.fasta'%sys.argv[1],'r')
for fa_file in fa_list.read().split():
	name = fa_file.split('/')[-1].split('.')[0]
	chrom = name.split('_')[0]
	index_dict[chrom] += 1
	seq_dict[name] = read_fa(fa_file)
fa_list.close()

for i in range(3,4):
	chrom = 'chr' + '0' * (2 - len(str(i))) + str(i)
	print('>%s'%chrom)
	out_line = ''
	for index in range(0,index_dict[chrom]):
		out_line += seq_dict['%s_%s'%(chrom,index)]
	print(out_line)
