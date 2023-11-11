#To lunch the api python -m uvicorn main:app --reload or uvicorn main:app --reload
#requiremnts : 
# fastapi :
#uvicorn :
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from IPS_ASTRE import transform_to_data_structure, ips_keywords, astre_keywords
from typing import List, Dict, Union, Tuple
from pydantic import BaseModel
from typing import List

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

def body_to_dictionnary(body):
    dic = {}
    for i in range(len(body.hypothesis)):
        dic[tuple(body.hypothesis[i])] = body.weight[i]
    return dic

# @app.get("/")
# async def root():
#     return [transform_to_data_structure()]

@app.get("/student")
async def root():
    global ips_keywords
    global astre_keywords
    datas = transform_to_data_structure(ips_keywords=ips_keywords, astre_keywords=astre_keywords)
    return [{"student": k, "prediction" : v[0], "score": v[1]} for k, v in datas.items()]

        

@app.get("/hypothesis/{variable}", response_model=List[Dict[str, Union[Tuple[str, ...], int]]])
async def root(variable: str):
    if (variable == "ips"):
        return [{"hypothesis": k, "value": v} for k, v in ips_keywords.items()]
    if(variable =="astre"):
        return [{"hypothesis": k, "value": v} for k, v in astre_keywords.items()]
   
class Etu(BaseModel):
    hypothesis : List
    weight : List
    
@app.post("/studentUpdate")
async def update(body: Etu):
    global ips_keywords
    global astre_keywords
    if (body.weight[0]<0):
        astre_keywords = body_to_dictionnary(body)
    else:
        ips_keywords = body_to_dictionnary(body)
    datas = transform_to_data_structure(ips_keywords=ips_keywords, astre_keywords=astre_keywords)
    return [{"student": k, "prediction" : v[0], "score": v[1]} for k, v in datas.items()]

# class Etu(BaseModel):
#     etu: str
#     num: int
#     affaires: list

# @app.post('/test')
# async def test(body: Etu):
#     print(body)
#     return body

    
 
