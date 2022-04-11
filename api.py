from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/", status_code=200)
def root ():
  return {"msg": "Hello World"}


@app.get("/amir", status_code=200)
def amir ():
  return {"msg": "I am amirali from Iran"}
