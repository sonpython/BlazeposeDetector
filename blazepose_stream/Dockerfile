FROM python:3.10

# Install system dependencies for OpenCV
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libgtk2.0-dev \
    libgl1-mesa-glx

# Copy the required files from the local directory into the container
COPY . /usr/src/app/

# Set the working directory
WORKDIR /usr/src/app/

# Install the required Python libraries
RUN pip install --no-cache-dir opencv-python-headless mediapipe flask gunicorn gevent

# Command to run the application
CMD ["gunicorn", "-b", "0.0.0.0:5001", "blazepose_stream:app", "-b", "gevent", "--timeout", "120"]
