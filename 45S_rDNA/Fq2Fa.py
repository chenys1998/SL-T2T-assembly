import sys,gzip

state = 0
fq = gzip.open(sys.argv[1],'rb')
##ONT reads files in fastq format

length = open('ONT_reads.len','w')
fa = open('ONT_reads.fa','w')
for line in fq:
	line = line.decode('utf-8')
	content = line.strip()
	if content.startswith('@'):
		name = content.strip('@')
		state = 1
	elif state == 1:
		state = 1
		if all(term in 'ATCG' for term in content[0:20]):
			print('>%s'%name,file = fa)
			print(content,file = fa)
			print(name,len(content),sep = '\t',file = length)
fq.close()
