#Use an official Python runtime as a parent image
FROM python:3.10-bullseye

#Set the working directory in the container
WORKDIR /app

#Copy the current directory contents into the container at /app
COPY  . /app/

#install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --progress-bar off -r requirements.txt

#Make port available to the world outside this container
EXPOSE 8080

#Run app.py when the container launches
CMD [ "python", "app.py" ]