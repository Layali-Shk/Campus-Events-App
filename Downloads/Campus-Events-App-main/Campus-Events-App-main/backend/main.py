from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Campus Events API is running"}
