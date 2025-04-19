from fastapi import FastAPI, UploadFile, File, Form
import shutil
from datetime import datetime

app = FastAPI()

@app.post("/upload-data/")
async def upload_data(device_id: str = Form(...), file: UploadFile = File(...)):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"device_{device_id}_{timestamp}.txt"

    
    with open(filename, "w") as out_file:
        content = await file.read()
        text_data = content.decode("utf-8")

        out_file.write(f"Device ID: {device_id}\n")
        out_file.write(f"Uploaded At: {timestamp}\n\n")
        out_file.write(text_data)

    return {"status": "success", "message": f"Data saved to {filename}"}
