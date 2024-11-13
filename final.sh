# Container ID
CONTAINER_ID=bd-a1-container

# Local directory where want to copy files
LOCAL_DIRECTORY=service-result/

# Create the local directory if not exist
mkdir -p $LOCAL_DIRECTORY

# Check if the container is running if not start run
if [ ! "$(docker ps -q -f id=$CONTAINER_ID)" ]; then
    echo "starting container..."
    docker start $CONTAINER_ID
fi

# Copy the output files from the container to the local machine
docker cp $CONTAINER_ID:/home/doc-bd-a1/eda-in-1.txt $LOCAL_DIRECTORY
docker cp $CONTAINER_ID:/home/doc-bd-a1/k.txt $LOCAL_DIRECTORY
docker cp $CONTAINER_ID:/home/doc-bd-a1/vis.png $LOCAL_DIRECTORY
docker cp $CONTAINER_ID:/home/doc-bd-a1/res_dpre.csv $LOCAL_DIRECTORY

# Stop the container
docker stop $CONTAINER_ID

echo "Files copied successfully and container stopped."
