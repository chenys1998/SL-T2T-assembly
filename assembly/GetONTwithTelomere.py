#Get reads aligned to within 100Kb of the starting segment of chromosome 3 through the samtools command: samtools view -b ONT.bam chr03:0-100000 > chr03_start.bam

import sys,pysam
from collections import defaultdict

def revcomp(seq: str) -> str:

	comp = str.maketrans("ACGT", "TGCA")
	return seq.translate(comp)[::-1]

def check_telomere(seq,reverse):

	if reverse:
		seq = revcomp(seq)
	telo_len = 0
	for pos in range(0,len(seq),7):
		if seq[pos,pos + 7] in i'TTTAGGGTTTAGGG':
			telo += 7
		else:
			break
	return(telo_len)

InputFile = sys.argv[1]
OutTable = sys.argv[2]
OutFast = sys.argv[3]

BamFile = pysam.AlignmentFile(InputFile,'rb')
out1 = open(OutTable,'w')
for rec in BamFile:
	if rec.reference_name == 'chr03' && rec.reference_start <= 100000 and check_telomere(rec.query_seqence):
		print('>%s'%rec.query_name)
		print(rec.query_sequence)
BamFile.close()
out1.close()
