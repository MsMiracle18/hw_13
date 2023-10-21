from fastapi import FastAPI, , HTTPException, Request
from fastapi.middleware.throttle import Throttle, SimpleThrottleLimiter

from app.routes import users

app = FastAPI()

app.include_router(users.router, prefix='/api')
app.include_router(auth.router, prefix='/api')

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# обмежити кількість запитів до 10 на хвилину на IP-адресу
app.add_middleware(Throttle, throttler=SimpleThrottleLimiter(rate="10/minute"))

@app.get("/contacts/")
async def get_contacts(request: Request):
    return {"message": "Contacts retrieved"}
