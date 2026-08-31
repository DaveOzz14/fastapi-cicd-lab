from fastapi import FastAPI

app = FastAPI(title="FastAPI CI/CD Lab")


@app.get("/")
def root():
    return {
        "message": "Hello from FastAPI"
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "id": user_id,
        "name": "David"
    }