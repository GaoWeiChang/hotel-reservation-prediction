FROM python:slim

# environment variable setting
ENV PYTHONDONTWRITEBYTECODE = 1 \ 
    PYTHONUNBUFFERED = 1

# working directory
WORKDIR /app

# install package
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# copy all file from local folder to /app folder in container
COPY . .

# installs the package in "editable" mode using setup.py 
# and prevents pip from storing downloaded packages in cache
RUN pip install --no-cache-dir -e .

RUN python pipeline/training_pipeline.py


# use port 8080 for this container
EXPOSE 8080

# run the app, when container run
# ['python', 'application.py'] = python application.py
CMD ['python', 'application.py']