from sqlalchemy.orm import Session
from sqlalchemy import delete
from . import models
import random

def query_user(db: Session, username: str):
    return db.query(models.login).filter(models.login.username == username).first()

def random_rock(db: Session):
    rocks = db.query(models.rocks).all()
    return random.choice(rocks)

def random_rock_by_tag(tag,db:Session):
    tagg = tag.split(',')
    #prob a better way to do this idk
    rock_list = []
    for i in tagg:
        rock_list.append(db.query(models.tags).filter(models.tags.tags == str(i.lower())).all())
    rand_tag = random.choice(rock_list)
    if rand_tag == []:
        return 404
    choice_of_rock = random.choice(rand_tag)
    return db.query(models.rocks).filter(models.rocks.name == choice_of_rock.name).first()

def search_rock(rock_name,db:Session):
    return db.query(models.rocks).filter(models.rocks.name == rock_name).first()

def add_rock(name,description,url,db:Session):
    rock = models.rocks(name=name.lower(),description=description,image_url=url)
    db.add(rock)
    db.commit()
    db.refresh(rock)
    return 200

def update_rock(name,drop,update,db:Session):
    rock = db.query(models.rocks).filter(models.rocks.name == name).first()
    if not rock:
        return "Rock not found."
    if drop == "name":
        rock.name=update
    elif drop == "description":
        rock.description=update
    elif drop == "image_url":
        rock.image_url=update
    else:
        return None
    db.commit()

    return 200