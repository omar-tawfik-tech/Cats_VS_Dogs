from fastapi import FastAPI ,Query
from pydantic import BaseModel,Field
from typing import Union
from typing_extensions import Annotated
app = FastAPI()

photos_dp = {"Photo":"cat"}
@app.get("/")
async def root(): # End Point

 return {"message":"Welcome To Cats VS Dogs WebSite"}

class Photo(BaseModel):

 Type : str = Field(title="The Type Of Pet",max_length=20,min_length=3)


@app.post("/photos")
async def Add_Photo(photo:Photo):
 Type = Photo.Type


 photos_dp.append({"Type":Type})
 return{"Message":"Pet Added Succsesfully","Pet: ":Photo}