Install requirements
============

workon hg19
pip install -r requirements.txt


Install postBIS
============

svn co https://colab.mpi-bremen.de/postbis/svn/trunk postbis
make
make install
createdb hg19 #creates the postgresql database
psql hg19
# in postgresql shell
CREATE EXTENSION postbis;


Download/Load data
============

workon hg19
cd scripts
./download_and_load_chromosomes.sh #it takes a long time
If you want to upload only a chromosome you can do this:
./download_and_load_chromosomes.sh M #downloads only the specified chromosome
