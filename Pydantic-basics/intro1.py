from pydantic import BaseModel

class Person(BaseModel):
    name : str
    age : int
    city : str

person = Person(name="Siddhu", age=24, city="Hyderabad")
print(person)

#-----------

from typing import Optional

class Employee(BaseModel):
    id : int
    name : str
    age : int
    city : str
    salary : Optional[float] = None
    is_active : Optional[float] = True

emp1 = Employee(id=1,name="siddhu",age=24, city="Hyd")
print(emp1)

#-------------
from typing import List

class ClassRoom(BaseModel):
    room_num : str
    students : List[str]
    capacity : int

class1 = ClassRoom(room_num="A101", students=["Sid","Mad","Su"], capacity= 30)

print(class1)

#------------------
from pydantic import BaseModel,Field

class Item(BaseModel):
    name: str=Field(min_length=2, max_length=50)
    price : float=Field(gt=0,le=1000)
    quantity : int=Field(ge=0)

item = Item(name="Book", price=2, quantity=10)
print(item)