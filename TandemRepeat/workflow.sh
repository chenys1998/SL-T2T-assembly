## TRF.gff = TRF output file.

python SortTRF.py TRF.gff > TRF_sorted.tab

awk '{if($2>100000) print$1}' TRF_sorted.tab |while read id;do(
python GetBED.py TRF.gff $id > bed/${id}.bed
bedtools getfasta -bed bed/${id}.bed -fi SL-T2T.fa -fo fa/${id}.fa -nameOnly -s
kalign --type dna -i fa/${id}.fa -o kalign/${id}.FA
python GetRepresent.py kalign/${id}.FA >> represent.fa)done

python GetDouble.py represent.fa > represent_double.fa
makeblastdb -in represent_double.fa -dbtype nucl -out represent_doube
blastn -db represent_double -query represent.fa -out blast.tab -outfmt 6
python GetFaNum.py represent_double.fa fa > double.tab
python FilterBlast.py double.tab blast.tab > target.list
