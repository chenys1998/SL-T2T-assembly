python Fq2Fasta.py ONT.fastq.gz
barrnap --kingdom euk ONT.fa > rdna.gff
python GFFto45S.py rdna.gff
python Get45SunitBED.py rdna.gff 45s.bed
bedtools getfasta -bed 45S_unit.bed -fi ONT.fa -fo 45s_unit.fa -nameOnly -s
python Split45SFA.py 45s_unit.fa

ls split/*.fa |while read id;do(
file=${id#*/}
prefix=${file%.*}
kalign --type dna -n 4 -i $id -o kalign/${prefix}.FA
python Kalign2Var.py kalign/${prefix}.FA var/${prefix}.tab
python Var2Represent.py var/${prefix}.tab represent/${prefix}.fa represent/${prefix}.txt $prefix
)done

cat represent/*.fa > represent/all.fa
kalign --type dna -n 4 -i represent/all.fa -o kalign/all.FA
python MergerResult.py represent/ kalign/all.FA 45S_rDNA.result
