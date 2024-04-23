#Use an official Python runtime as a parent image
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and data file into the container
COPY word_analysis.py /app
COPY paragraphs.txt /app

# Install any dependencies required by the Python script
RUN pip install nltk

# Download the required data files for nltk
RUN python -m nltk.downloader -d /usr/local/share/nltk_data punkt stopwords

# Command to run the Python script
CMD ["python","word_analysis.py"]