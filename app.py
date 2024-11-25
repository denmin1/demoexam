import datetime
from typing import Annotated, Optional
from pydantic import BaseModel
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

class Order(BaseModel):
 number : int
 startdate : datetime.date
 device : str
 problemtype : str
 description : str
 client : str
 status : str
 master : Optional[str] = "Не назначен"
 comments : Optional[str] = []


class UpdateOrederDTO(BaseModel):
 number : int
 status : Optional[str] = ""
 description : Optional[str] = ""
 master : Optional[str] = ""
 comment : Optional[str] = str

repo=[
 
Order(
 number = 1,
 startdate = "2000-12-01",
 device = "testdev",
 problemtype = "testprobl",
 description = "test",
 client = "ivan",
 status = "testovy"
),

Order(
 number = 2,
 startdate = "2000-12-01",
 device = "testdev",
 problemtype = "testprobl",
 description = "test",
 client = "ivan",
 status = "testovy"
),

Order(
 number = 3,
 startdate = "2000-12-01",
 device = "testdev",
 problemtype = "testprobl",
 description = "test",
 client = "ivan",
 status = "testovy"
)

]

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins = ["*"],
  allow_methods = ["*"],
  allow_headers = ["*"]
  )


message = ""

 
@app.get("/orders")
def get_orders(param = None):
 global message
 buf = message
 message = ""
 if (param):
    return {"repo": [o for o in repo if o.number == int(param)], "message": buf}
 return {"repo": repo, "message": buf}

@app.post("/orders")
def create_order(dto : Annotated[Order, Form()]  ):
 repo.append(dto)



@app.post("/update")
def update_order(dto : Annotated[UpdateOrederDTO, Form()]  ):
 global message
 for o in repo:
  if o.number == dto.number:
    if dto.status != o.status and dto.status != "":
      o.status = dto.status
      message += f"Статус заявки {o.number} изменен\n" 
      if(o.status == "выполнено"):
         message += f"Заявка №{o.number} завершена\n"
    if dto.description != "":
      o.description = dto.description
    if dto.master != "":
      o.master = dto.master
    if dto.comment != None and dto.comment != "":
      o.comments.append(dto.comment)
    return o
 return "Не найдено"
