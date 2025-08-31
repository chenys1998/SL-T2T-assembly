import sys,os
from collections import defaultdict
from time import sleep

tab = open(sys.argv[1],'r')
for line in tab:
	contents = line.strip().split()
	index = 0
	start = 1
	chrom = contents[0]
	length = int(contents[1])
	while start + 4999999 < length:
		end = start + 4999999
		os.system("bsub -q standardB -n 1 -o log/%s_%s.log 'java -Xmx16G -jar /public-supool/software/pilon-1.22.jar --genome pre_pilon.fa --frags bwa.bam --targets %s:%s-%s --outdir out/ --output %s_%s'"%(chrom,index,chrom,start,end,chrom,index))
		sleep(1)
		index += 1
		start += 5000000
	else:
		end = length
		os.system("bsub -q standardB -n 1 -o log/%s_%s.log 'java -Xmx16G -jar /public-supool/software/pilon-1.22.jar --genome pre_pilon.fa --frags bwa.bam --targets %s:%s-%s --outdir out/ --output %s_%s'"%(chrom,index,chrom,start,end,chrom,index))
		sleep(1)
tab.close()
