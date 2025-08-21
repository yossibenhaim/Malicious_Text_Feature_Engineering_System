#Lib's
import uvicorn
#Classes
import routse

app = routse.app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)