from fastapi import FastAPI

app = FastAPI(
    title="Production CI/CD Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Production CI/CD Platform",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }