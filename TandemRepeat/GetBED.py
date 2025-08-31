import sys

index = 0
gff = open(sys.argv[1],'r')
for line in gff:
	contents = line.strip().split()
	if contents[8].split(';')[0].split('@')[1] == sys.argv[2]:
		index += 1
		if int(contents[3]) < int(contents[4]):
			print(contents[0],int(contents[3]) - 1,contents[4],'%s_%s'%(sys.argv[2],index),'1',contents[6],sep = '\t')
		elif contents[6] == '+':
			print(contents[0],int(contents[4]) - 1,contents[3],'%s_%s'%(sys.argv[2],index),'1','-',sep = '\t')
		else:
			print(contents[0],int(contents[4]) - 1,contents[3],'%s_%s'%(sys.argv[2],index),'1','+',sep = '\t')
gff.close()
