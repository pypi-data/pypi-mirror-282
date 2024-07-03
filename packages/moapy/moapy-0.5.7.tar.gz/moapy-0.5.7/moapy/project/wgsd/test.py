from pydantic import BaseModel, Field
from typing import List
from dataclasses import dataclass, field

class Force(BaseModel):
    Nz: float = 0.0
    Mx: float = 0.0
    My: float = 0.0

class Lcom(BaseModel):
    name: str = Field(default="lcom", description="load combination name")
    f: Force = Field(default=Force(), description="load combination force")

class Lcb(BaseModel):
    uls: list[Lcom] = Field(default=[], description="uls load combination")

    class Config:
        title = "GSD Load Combination"

class DataClassA(BaseModel):
    lcb: Lcb = field(default=Lcb(uls=[
        Lcom(name="uls1", f=Force(Nz=100.0, Mx=10.0, My=50.0)),
        Lcom(name="uls2", f=Force(Nz=100.0, Mx=15.0, My=50.0))
    ]))

class DataClassB(BaseModel):
    lcb: Lcb = field(default_factory=lambda: Lcb(uls=[
        Lcom(name="uls3", f=Force(Nz=200.0, Mx=20.0, My=100.0)),
        Lcom(name="uls4", f=Force(Nz=200.0, Mx=25.0, My=100.0))
    ]))

# DataClassA와 DataClassB 객체 생성
data_a = DataClassA()
data_b = DataClassB()

print(data_a)
print(data_b)
