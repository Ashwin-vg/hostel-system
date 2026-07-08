from fastapi import HTTPException

ADMIN = {"username": "admin", "password": "1234"}

def login_check(username, password):
    if username == ADMIN["username"] and password == ADMIN["password"]:
        return True
    raise HTTPException(status_code=401, detail="Invalid login")