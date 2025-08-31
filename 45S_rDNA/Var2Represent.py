import sys

txt = open(sys.argv[1],'r')
out1 = open(sys.argv[2],'w')
out2 = open(sys.argv[3],'w')
sample_name = sys.argv[4]
print('>%s'%sample_name,file = out1)
seq = ''
index = 0
for line in txt:
	contents = line.strip().split()
	if line.startswith('#'):
		continue
	if contents[1].split('/')[0] != '-' or float(contents[2].split('/')[1]) >= 0.01:
		index += 1
		print(index,line.strip(),sep = '\t',file = out2)
		if contents[1].split('/')[0] != '-':
			seq += contents[1].split('/')[0]
		else:
			seq += contents[1].split('/')[1]
print(seq,file = out1)
txt.close()
out1.close()
out2.close()
