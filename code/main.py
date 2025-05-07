from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
from fastapi import HTTPException
from fastapi.responses import Response
from typing import Optional

app = FastAPI()

@app.get("/words/", response_model=List[str])
def get_words(start_by : str = None, length_min : int = None):
    w = [w for w in ["Hello", "Bonjour", "Hola"] 
         if (start_by is None or w.startswith(start_by)) and 
         (length_min is None or len(w) >= length_min)]        
    return w


# Modèle de ville
class City(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=1)
    npa: str = None

class CityOut(BaseModel):
    name: str
    npa: str


# Modèle de personne avec une ville
class Person(BaseModel):
    id: int = Field(gt=0)
    name: str
    age: int
    #city: City

# Données simulées
cities = [
    City(id=1, name="Lausanne", npa="1000"),
    City(id=2, name="Genève", npa="1200"),
    City(id=3, name="Fribourg", npa="1700"),
]

persons = [
    Person(id=1, name="Alice", age=30, city=cities[0]),
    Person(id=2, name="Bob", age=25, city=cities[1]),
    Person(id=3, name="Charlie", age=40, city=cities[2]),
]


persons = [
    Person(id=1, name="Alice", age=30),
    Person(id=2, name="Bob", age=25),
    Person(id=3, name="Charlie", age=40),
]



# Routes de l'API
@app.get("/persons", response_model=List[Person])
def get_persons():
    return persons

@app.get("/cities", response_model=List[CityOut])
def get_cities():
    return cities

@app.post("/cities", response_model=City)
def create_city(city: City):
    cities.append(city)
    return city

@app.post("/persons", response_model=Person)
def create_person(person: Person):
    persons.append(person)
    return person

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204)