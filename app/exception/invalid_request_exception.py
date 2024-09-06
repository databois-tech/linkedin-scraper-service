from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()


class InvalidRequestException(Exception):
    def _init_(self, status_code=400, detail=""):
        self.status_code = status_code
        self.detail = detail