from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import  Image
import tensorflow as tf

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image





CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

MODEL = tf.keras.models.load_model("../saved_models/1")

app = FastAPI()

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    image  =read_file_as_image( await file.read())
    return



if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
