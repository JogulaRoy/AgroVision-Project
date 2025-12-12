from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Sample disease database
disease_database = [
    {
        "name": "Late Blight",
        "description": "Late blight is a potentially devastating disease of potato and tomato...",
        "treatments": [
            "Apply fungicides containing chlorothalonil or copper compounds.",
            "Destroy infected plant parts.",
            "Avoid overhead irrigation."
        ]
    },
    {
        "name": "Powdery Mildew",
        "description": "Powdery mildew appears as white powdery growth on leaf surfaces...",
        "treatments": [
            "Use sulfur-based fungicides.",
            "Improve air circulation.",
            "Apply neem oil."
        ]
    },
    {
        "name": "Rust",
        "description": "Rust appears as orange-brown pustules on leaves, reducing yield...",
        "treatments": [
            "Spray triazole fungicides.",
            "Rotate crops.",
            "Plant resistant varieties."
        ]
    },
    {
        "name": "Fusarium Wilt",
        "description": "Soil-borne fungus causes yellowing and wilting, blocking water flow...",
        "treatments": [
            "Remove infected plants.",
            "Rotate crops for 5 years.",
            "Sterilize tools."
        ]
    }
]

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Simulate prediction
    disease = random.choice(disease_database)
    confidence = random.randint(80, 99)

    return JSONResponse({
        "name": disease["name"],
        "description": disease["description"],
        "treatments": disease["treatments"],
        "confidence": confidence
    })
