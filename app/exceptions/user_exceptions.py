from fastapi import HTTPException

class UserNotFound(HTTPException):
    def __init__(self, detail: str = "User not found"):
        super().__init__(status_code=404, detail=detail)

class UserAlreadyExists(HTTPException):
    def __init__(self, detail: str = "Email already registered"):
        super().__init__(status_code=400, detail=detail)
