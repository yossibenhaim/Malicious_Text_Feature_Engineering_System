from fastapi import FastAPI, HTTPException

from manager import Manager
from utils import  Utils

manager = Manager()
app = FastAPI()

@app.get("/")
def get_root():
    return {'Hello':'World'}


#Read
#All
@app.get("/get_data")
async def get_all_data():
    try:
        res = manager.get_data_from_mongo()
        return {'soldiers':res}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail={"error": str(e)})