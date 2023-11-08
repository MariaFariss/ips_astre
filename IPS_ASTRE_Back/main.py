#To lunch the api python -m uvicorn main:app --reload or uvicorn main:app --reload
#requiremnts : 
# fastapi :
#uvicorn :
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from IPS_ASTRE import transform_to_data_structure
app = FastAPI()

#for the corse :
app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def root():
    return [transform_to_data_structure()]
