from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Product(BaseModel):
    name: str
    url: str
    imageUrl: str
    price: float


@app.get("/")
def home():
    return RedirectResponse("/docs")

@app.get("/test")
def test() -> Product:
    return Product(
        name="Test",
        url="google.com",
        imageUrl="https://upload.wikimedia.org/wikipedia/en/9/9a/Trollface_non-free.png",
        price=0
    )

def main():
    uvicorn.run(app, host='0.0.0.0', port=8000)


if __name__ == "__main__":
    main()
