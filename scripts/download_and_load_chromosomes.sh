#!/usr/bin/env bash

BASE_URL="http://hgdownload.soe.ucsc.edu/goldenPath/hg19/chromosomes/"

if [ $# -eq 0 ]
then
    FILES[0]="chr1.fa.gz"
    FILES[1]="chr2.fa.gz"
    FILES[2]="chr3.fa.gz"
    FILES[3]="chr4.fa.gz"
    FILES[4]="chr5.fa.gz"
    FILES[5]="chr6.fa.gz"
    FILES[6]="chr7.fa.gz"
    FILES[7]="chr8.fa.gz"
    FILES[8]="chr9.fa.gz"
    FILES[9]="chr10.fa.gz"
    FILES[10]="chr11.fa.gz"
    FILES[11]="chr12.fa.gz"
    FILES[12]="chr13.fa.gz"
    FILES[13]="chr14.fa.gz"
    FILES[14]="chr15.fa.gz"
    FILES[15]="chr16.fa.gz"
    FILES[16]="chr17.fa.gz"
    FILES[17]="chr18.fa.gz"
    FILES[18]="chr19.fa.gz"
    FILES[19]="chr20.fa.gz"
    FILES[20]="chr21.fa.gz"
    FILES[21]="chr22.fa.gz"
    FILES[22]="chrM.fa.gz"
    FILES[23]="chrX.fa.gz"
    FILES[24]="chrY.fa.gz"
else
    FILES[0]="chr$1.fa.gz"
fi

for F in "${FILES[@]}"
do
    wget "$BASE_URL$F"
    gzip -f -d $F

    #upload data
    SPLIT=`echo $F | cut -d'.' -f 1`
    CHROMOSOME=`echo $SPLIT | cut 3`
    CHROMOSOME=${SPLIT:3}
    NF="chr$CHROMOSOME.fa"
    P=`pwd`/
    ../manage.py load_chromosome --path "$P$NF" --chromosome $CHROMOSOME --convert_to_upper t hg19
    ../manage.py load_postbis_chromosome --path "$P$NF" --chromosome $CHROMOSOME hg19
done
