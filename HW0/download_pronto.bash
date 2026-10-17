mkdir pronto
cd pronto
echo "cd pronto moves your working directory to the newly created pronto 
directory" > README.txt
mkdir data
cd data
curl -O https://s3.amazonaws.com/pronto-data/open_data_year_one.zip
unzip ./open_data_year_one.zip
head 2015_trip_data.csv

