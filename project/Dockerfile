FROM python:3.12.3-alpine

WORKDIR /usr/src/app

# Copy the requirements file from the parent directory
COPY ./requirements.txt /usr/src/app/requirements.txt

# prevent python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# ensure python output is sent directly to the terminal without buffering
ENV PYTHONUNBUFFERED 1

# Combine RUN commands to minimize layers and set permissions for entrypoint.sh
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /usr/src/app/
