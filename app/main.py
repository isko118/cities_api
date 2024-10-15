import logging
import sys

import uvicorn
from fastapi import FastAPI

from app.routes import router

app = FastAPI()
app.include_router(router)

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    uvicorn.run(app, host='0.0.0.0', port=8000)
