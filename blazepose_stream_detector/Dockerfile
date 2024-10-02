FROM python:3.10-slim

WORKDIR /usr/src/app

# Install necessary packages
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Copy required files into the container
COPY blazepose_stream_detector/ /usr/src/app/

# Install Python libraries
RUN pip install --no-cache-dir opencv-python-headless mediapipe flask gunicorn

# Run script
CMD ["bash", "run.sh"]
