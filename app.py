import datetime
from typing import Annotated, Optional
from pydantic import BaseModel
from fastapi import FastAPI, Form

class Order(BaseModel):
 number : int
 startdate : datetime.date
 device : str
 problemtype : str
 description : str
 client : str
 status : str
 master : Optional[str] = "Не назначен"


class UpdateOrederDTO(BaseModel):
 number : int
 status : Optional[str] = ""
 description : Optional[str] = ""
 master : Optional[str] = ""




repo=[
 
Order(
 number = 1,
 startdate = "2000-12-01",
 device = "testdev",
 problemtype = "testprobl",
 description = "test",
 client = "ivan",
 status = "testovy"
)

]

app = FastAPI()
 
@app.get("/orders")
def get_orders():
 return repo

@app.post("/orders")
def create_order(dto : Annotated[Order, Form()]  ):
 repo.append(dto)



@app.post("/update")
def update_order(dto : Annotated[UpdateOrederDTO, Form()]  ):
 for o in repo:
  if o.number == dto.number:
    if dto.status != o.status and dto.status != "":
      o.status = dto.status
    if dto.description != "":
      o.description = dto.description
    if dto.master != "":
      o.master = dto.master
    return o
 return "Не найдено"
