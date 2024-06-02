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
