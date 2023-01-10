from sqlalchemy.orm import Session
from sqlalchemy import delete
from . import models, schemas
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
    return db.query(models.rocks).filter(models.rocks.name == rock_name.lower()).first()