from fastapi import FastAPI
from fastapi.responses import FileResponse
app = FastAPI()

@app.get("/")
def read_root() :
    return FileResponse("index.html")

@app.get("/file/{file_name}")
def getfile(file_name : str, q : str):
    if(q == "luca_pass"):
        return FileResponse(file_name)
    else :
        return "拒绝访问"



