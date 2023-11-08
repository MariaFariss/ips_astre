#To lunch the api python -m uvicorn main:app --reload or uvicorn main:app --reload
#requiremnts : 
# fastapi :
#uvicorn :
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from IPS_ASTRE import transform_to_data_structure, ips_keywords, astre_keywords
from typing import List, Dict, Union, Tuple

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



# @app.get("/")
# async def root():
#     return [transform_to_data_structure()]

@app.get("/")
async def root():
    data = transform_to_data_structure()
    return [{"student ": k, "prediction " : v[0], "score ": v[1]} for k, v in data.items()]


@app.get("/hypothesis/{variable}", response_model=List[Dict[str, Union[Tuple[str, ...], int]]])
async def root(variable: str):
    if (variable == "ips"):
        return [{"hypothesis": k, "value": v} for k, v in ips_keywords.items()]
    if(variable =="astre"):
        return [{"hypothesis": k, "value": v} for k, v in astre_keywords.items()]