from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn
from ikeatypes import *

app = FastAPI()


@app.get("/", include_in_schema=False)
def home():
    return RedirectResponse("/docs")

    )

def main():
    try:
        uvicorn.run(app, host='0.0.0.0', port=8000)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
