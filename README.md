## Brief description

The goal is to establish a local dockerized environment for data analysis on a dataset. The goal is to automate the data preprocessing, EDA, visualization and ML model (K-means clustering algorithm). This one contains writing a dockerfile which includes required python libraries such as Pandas, Numpy and scikit-learn, and together with creating the directory that the dataset will live in inside from within the container. This consists of multiple Python scripts to dynamically read the dataset, clean and transform data, EDA, data visualization as well as K-means algorithm for clustering. Also, we use bash scripts to help transfer output files from the container to our local machine.

## Contributors

| Name                    | ID         | E-Mail                     |
|-------------------------|------------|----------------------------|
| Shrouk Anwar Gbr        | 211001720  | S.Anwar2120@nu.edu.eg      |
| Zeinab Mostafa Omran    | 211001793  | z.mostafasayed2193@nu.edu.eg|
| Mariam Mohamed Farhat  | 211001971  | m.mohamed2171@nu.edu.eg    |
| Zahraa Mohamed Mosa     | 211001602  | z.mohamed2102@nu.edu.eg    |

## To start up the Docker Image
use the following command
```bash
./startup.sh
```
## Building the Docker Image
use the following command
```bash
docker start bd-a1-container
docker build -t bd-a1-image .
```
## Running the Docker Container
use the following command
```bash
docker run -it bd-a1-image
```
# Execute the pipeline
use the following command
```bash
python3 load.py titanic.csv
```
## Listing All Containers
use the following command
```bash
docker ps -a
```
## Retrieve Output Files , Copy the output files from the container to the local machine
use the following command
```bash
./final.sh
```

## Docker Hub
You can pull the image from Docker Hub from [here](https://hub.docker.com/r/shroukgbr89/bd-a1-image)

## Github
You can access the repo from Github from [here](https://github.com/shroukgbr89/assignment1_bigdata) or use the following command

## License
[MIT](https://choosealicense.com/licenses/mit/)