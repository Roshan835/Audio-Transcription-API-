FROM python:3.10-slim

WORKDIR /python-docker

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install git -y

RUN pip install -r requirements.txt

RUN pip install "git+https://github.com/openai/whisper.git"

RUN apt-get update && apt-get install -y ffmpeg

COPY . . 

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["fast_api:app", "--host", "0.0.0.0", "--port", "8000"]


