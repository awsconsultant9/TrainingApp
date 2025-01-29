from fastapi import FastAPI, Cookie, Response, Depends, HTTPException
from pydantic import BaseModel
from models import User
from sqlalchemy.orm import Session
from database import SessionLocal
from typing import Annotated
app = FastAPI()

class Event(BaseModel):
    event_name: str
    event_status: str
    event_id: int
    valid_event: bool

class UserCreate(BaseModel):
    name: str
    id: int
    email: str



# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoint to create a new user
@app.post("/users/", response_model=UserCreate)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists (optional)
    db_user = db.query(User).filter(User.email == user.email).first()
    # print(db_user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create a new SQLAlchemy User instance
    db_user = User(name=user.name, email=user.email)

    # Add the user to the session and commit to the database
    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # This will refresh the instance with the generated ID

    return db_user  # Returning the created user (or just a success message if preferred)


@app.post("/user/create")
async def usercreate(user:UserCreate):
    pass

@app.get("/")
async def root(event: Event):
    return event.event_name + event.event_status

@app.get("/event/{event_number}")
async def event_number(event_number: int):
    return "event number or event name is {0}".format(event_number)

@app.get("/even/{event_number}")
async def event_name(event_number: str):
    return "event number or event name is {0}".format(event_number)


@app.get("/eventqp")
async def qp(ename:str, eid:int):
    return ename+str(eid)+"peddii"


@app.get("/login/")
def login(response: Response):
    response.set_cookie(key="session_id", value="abc123", httponly=True)
    return {"message": "Logged in successfully"}

# Logout endpoint to clear session cookie
@app.get("/logout/")
def logout(response: Response):
    response.delete_cookie("session_id")
    return {"message": "Logged out successfully"}

@app.get("/qp")
async def qpprocess(a:int = 10 , b:int = 20):
    return f"sumofqp {a+b}"

@app.get("/awsserver")
async def aws():
    return {"subject":"this endpoint is from aws"}
