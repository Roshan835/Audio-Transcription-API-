# Transcription API with Whisper

This repository contains a FastAPI application that provides an endpoint for transcribing audio files using OpenAI's Whisper model. The API supports uploading multiple audio files and returns the transcriptions for each file.

## Features

- Transcribe audio files using OpenAI's Whisper model
- Support for multiple file uploads
- CUDA support for faster transcription if a compatible GPU is available
- Dockerized for easy deployment

## Requirements

fastapi
aiofiles
python-multipart
uvicorn

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/Roshan835/Audio-Transcription-API-.git
```

### Using Uvicorn Directly

Make sure you have Python and the required packages installed. You can create a virtual environment for this.

```bash
# Create a virtual environment
python -m venv env

# Activate the virtual environment
source env/bin/activate  # On Windows, use `env\Scripts\activate`

# Install the requirements
pip install -r requirements.txt

# Run the application with Uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Accessing the API
Once the container or application is running, you can access the API documentation at 'http://localhost:8000/docs'.

### Example Usage
To transcribe audio files, use the '/whisper' endpoint.
The API will return a JSON response with the filenames and their respective transcriptions.


