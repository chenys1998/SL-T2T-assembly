##Hifiasm assembly
hifiasm -t20 --ont -o Sol_ont.asm ONT.read.fastq.gz
python GetChromLen.py Sol_ont.asm.bp.p_ctg.fasta > Sol_ont_len.tab

##Telomere extend
minimap2 -ax map-ont -t 10 Sol_ont.asm.bp.p_ctg.fasta ONT.fastq --MD|samtools view -@ 20 -bS|samtools sort -@ 20 -o ont.bam
samtools index ont.bam
python GetONTwithTelomere.py ont.bam chr03start_ont.tab chr03start_ont.fa
minimap2 -x asm5 -I 1G -t 4 Sol_ont.asm.bp.p_ctg.fasta chr03start_ont.fa > minimap2.paf

##Pilon correct
bwa mem Sol_ont_len.tab -t 20 1706-4-5-6_R1.fq.gz 1706-4-5-6_R2.fq.gz |samtools view -@ 20 -bS|samtools sort -@ 20 -o bwa.bam
samtools index bwa.bam
python PilonCorrect.py Sol_ont_len.tab pilon/
python MergePilon.py pilon/ > pilon.fa

