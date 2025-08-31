makeblastdb -in SL-T2T.fa -dbtype nucl -out SL-T2T
blastn -query TRGIV.fa -db SL-T2T -out blast.tab -outfmt 6
python FilterBlast.py blast.tab > trgiv.tab
python GetChromLen.py SL-T2T.fa > SL-T2T_len.tab
python GetTRGIV.py SL-T2T_len.tab trgiv.tab > genome_trgiv.tab
