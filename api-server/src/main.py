from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"health": "OK"}

@app.get("/job")
def getJobs():
    return [{
        "id": "uid1",
        "title": "cinematographer",
        "description": "head of imagery",
        },{
        "id": "uid2",
        "title": "camera operator",
        "description": "operates camera",
        },{
        "id": "uid3",
        "title": "steadicam operator",
        "description": "smooth camera movement",
        }]
        

