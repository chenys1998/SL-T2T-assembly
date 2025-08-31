import sys

worked_num = 0
result_num = 1
fa = open(sys.argv[1],'r')
##All 45S_units sequence in fasta File.
out = open('split/split_%s.fa'%result_num,'w')
for line in fa:
	content = line.strip()
	if content.startswith('>'):
		worked_num += 1
		if worked_num > 1000:
			worked_num = 1
			out.close()
			result_num += 1
			out = open('split/split_%s.fa'%result_num,'w')
	print(content,file = out)
fa.close()
out.close()
