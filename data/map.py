from typing import Optional, List, Tuple

import json

from pydantic import BaseModel

class SolarObject(BaseModel):
    name : Optional[str]
    sprite : str
    distance : int
    period : int

class SolarSystem(BaseModel):
    name: str
    position : Tuple[int,int]
    governement: str
    links: Optional[List[str]]
    objects : List[SolarObject]

class Map(BaseModel):
    SolarSystems : List[SolarSystem]

file_name= "map.json"

def write_template():
    position = [0,0]
    links = ["a", "b"]
    so1 = SolarObject(name="a", sprite="a/b", distance=0, period=0)
    so2 = SolarObject(name="a", sprite="a/b", distance=0, period=0)

    s1 = SolarSystem(name="Sol", position=[0,0], governement="", links=links, objects=[so1, so2])
    s2 = SolarSystem(name="NA", position=[0,0], governement="", links=links, objects=[so1, so2])

    sslist = Map(SolarSystems = [s1,s2] )

    #print(ss.model_dump_json(indent=2))
    print(sslist.model_dump_json(indent=2))

    f = open(file_name, "w")
    f.write(sslist.model_dump_json(indent=2))

def read_file():
    with open(file_name) as f:
        file_data = json.load(f)
        map_data = Map(**file_data)

    #Check if completed
    print(map_data.SolarSystems[0])

if __name__ == "__main__":
    
    #write_template()

    read_file()


    

    