import uvicorn
from fastapi import FastAPI, HTTPException, Depends, Request,Form,status
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from tools import crud, models
from tools.data import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import Union
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel
import os
try: # railway doesnt have access to the env 
    from dotenv import load_dotenv
    load_dotenv()
    print("loaded")
except:
    print("not loaded")
    pass
models.Base.metadata.create_all(bind=engine)
Rock_API = FastAPI(docs_url=None)
templates = Jinja2Templates(directory="./templates")

class Settings(BaseModel):
    authjwt_secret_key: str = os.getenv('KEY')

    authjwt_token_location: set = {"cookies"}

    authjwt_cookie_csrf_protect: bool = False

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@AuthJWT.load_config
def get_config():
    return Settings()

@Rock_API.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


@Rock_API.get('/')
def root(request:Request):
    return templates.TemplateResponse("index.html", {"request":request})

@Rock_API.get('/login')
def login(request: Request):
    return templates.TemplateResponse('login.html',{"request": request})

@Rock_API.post('/login')
def login(request: Request,username: str = Form(...),password: str = Form(...), Authorize: AuthJWT = Depends(),db: Session = Depends(get_db)):
    is_user = crud.query_user(db,username)
    if not is_user:
        raise HTTPException(status_code=401,detail="Bad username or password")
    elif is_user.password != password:
        raise HTTPException(status_code=401,detail="Bad username or password")
    #setting cookies
    access_token = Authorize.create_access_token(subject=username)
    refresh_token = Authorize.create_refresh_token(subject=username)

    Authorize.set_access_cookies(access_token)
    Authorize.set_refresh_cookies(refresh_token)
    return RedirectResponse(request.url_for('protected'), status_code=status.HTTP_303_SEE_OTHER)    

@Rock_API.get('/refresh')
def refresh(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()

    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)

    Authorize.set_access_cookies(new_access_token)
    return {"msg":"The token has been refreshed"}

@Rock_API.get('/logout')
def logout(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    Authorize.unset_jwt_cookies()
    return {"msg":"Successfully logged out"}

@Rock_API.get('/panel')
def protected(request: Request,Authorize: AuthJWT = Depends()):

    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    return templates.TemplateResponse('admin.html',{"request": request,"user":current_user})

@Rock_API.get('/rock/random')
def get_rock(tags: Union[str, None] = None,db: Session = Depends(get_db)):
    if tags:
        rock = crud.random_rock_by_tag(tags,db)
        return {"msg": "Rock not found by tag. Try entering a valid tag."} if rock == 404 else rock
    return crud.random_rock(db)

@Rock_API.get('/rock/{rock_name}')
def get_rock(rock_name,db: Session = Depends(get_db)):
    return crud.search_rock(rock_name,db)




if __name__ == "__main__":
    uvicorn.run("main:Rock_API", host="0.0.0.0", port=os.getenv("PORT",default=8000))