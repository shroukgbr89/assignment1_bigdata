# Use the Ubuntu base image
FROM ubuntu:22.04

# Update packages and install Python and pip in a single step
RUN apt-get update -y && \
    apt-get install -y python3 python3-pip

# Install required Python libraries in one command
RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

# Create directory and copy dataset
RUN mkdir -p /home/doc-bd-a1/
COPY titanic.csv /home/doc-bd-a1/

# Set working directory
WORKDIR /home/doc-bd-a1/

# Copy all .py files
COPY load.py dpre.py eda.py vis.py model.py /home/doc-bd-a1/

# Set the python files
RUN python3 load.py titanic.csv

# Default command to open bash after running the script
CMD ["/bin/bash"]
