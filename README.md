Download data
============

Dowload and decompress this file http://hgdownload.soe.ucsc.edu/goldenPath/hg19/chromosomes/chr1.fa.gz


Install requirements
============

workon hg19
pip install -r requirements.txt


Upload data
============

workon hg19
This takes like 20 minutes.
To upload chromosome 1
./manage.py load_chromosome --path /path/to/chr1.fa --chromosome 1 
To upload chromosome 2
./manage.py load_chromosome --path /path/to/chr2.fa --chromosome 2
