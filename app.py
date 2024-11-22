from exceptiongroup import catch
from fastapi import FastAPI , HTTPException
from pydantic import BaseModel

app = FastAPI()
class DetectionModel(BaseModel):
    frames : list
    landmarks : list


@app.get("/")
async def home():
    return {
        "MESSAGE" : "START OF API "
    }

@app.post("/detection")
async def post_detection(detection : DetectionModel):
    try :
        return {
            'frames' : detection.frames ,
            'landmarks' : detection.landmarks
        }
    except HTTPException :
        return HTTPException(detail= "the list is Empty" , status_code=404)

