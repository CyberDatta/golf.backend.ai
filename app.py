
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


class LandmarksModel(BaseModel):
    x : float
    y : float
    z : float
    v : float
    p : float


class DetectionModel(BaseModel):
    frames: list[list[float]]
    landmarks: list[list[float]]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def home():
    return {
        "MESSAGE": "START OF API "
    }


@app.post("/detection")
async def post_detection(detection: DetectionModel):
    try:
        return {
            'frames': detection.frames,
            'landmarks': detection.landmarks
        }
    except HTTPException:
        return HTTPException(detail="the list is Empty", status_code=404)
