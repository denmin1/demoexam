import datetime
from typing import Annotated
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