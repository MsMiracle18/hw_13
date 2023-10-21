from fastapi import FastAPI, , HTTPException, Request
from fastapi.middleware.throttle import Throttle, SimpleThrottleLimiter
from fastapi.middleware.cors import CORSMiddleware

from app.routes import users
from decouple import config

# завантажити змінні середовища з .env файлу
DATABASE_URL = config('DATABASE_URL')
SECRET_KEY = config('SECRET_KEY')
CLOUDINARY_API_KEY = config('CLOUDINARY_API_KEY')
CLOUDINARY_API_SECRET = config('CLOUDINARY_API_SECRET')

# використати змінні середовища
print(DATABASE_URL)
print(SECRET_KEY)

app = FastAPI()

app.include_router(users.router, prefix='/api')
app.include_router(auth.router, prefix='/api')
# обмежити кількість запитів до 10 на хвилину на IP-адресу
app.add_middleware(Throttle, throttler=SimpleThrottleLimiter(rate="10/minute"))

# включити CORS. дозволити доступ з будь-якого джерела.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Можете вказати конкретні джерела, з яких дозволений доступ.
    allow_credentials=True,
    allow_methods=["*"],  # Дозволяємо будь-які HTTP методи (GET, POST, і таке інше).
    allow_headers=["*"],  # Дозволяємо будь-які HTTP заголовки.
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/contacts/")
async def get_contacts(request: Request):
    return {"message": "Contacts retrieved"}


