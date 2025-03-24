from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modèle de ville
class City(BaseModel):
    id: int
    name: str
    npa: str  # Numéro Postal d'Acheminement

# Modèle de personne avec une ville
class Person(BaseModel):
    id: int
    name: str
    age: int
    city: City

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

# Routes de l'API
@app.get("/persons", response_model=List[Person])
def get_persons():
    return persons

@app.get("/cities", response_model=List[City])
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