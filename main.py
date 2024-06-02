from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
from fastapi.responses import JSONResponse, RedirectResponse
import whisper
import torch
from tempfile import NamedTemporaryFile

# Check if CUDA is available and set device accordingly
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Load the Whisper model
model = whisper.load_model("base", device=DEVICE)

app = FastAPI()

@app.post("/whisper")
async def handler(files: List[UploadFile] = File(...)):
    if not files:
        raise HTTPException(status_code=400, detail="At least one file must be uploaded")

    results = []

    for file in files:
        with NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(file.file.read())
            temp_file.flush()  # Ensure all data is written to the file

            result = model.transcribe(temp_file.name)

            results.append(
                {
                    "filename": file.filename,
                    "transcript": result["text"]
                }
            )

    return JSONResponse(content={"results": results})

@app.get("/", response_class=RedirectResponse)
async def redirect_to_docs():
    return "/docs"
