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
        "status": "DOWN"
    }


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "id": user_id,
        "name": "David"
    }

@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }