from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import search, products
from config.settings import settings

def create_app() -> FastAPI:
    app = FastAPI(
        title="Image Search Engine",
        description="Text-to-Image Search Engine using CLIP",
        version="1.0.0"
    )

    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    app.include_router(search.router, prefix="/api/search", tags=["search"])
    app.include_router(products.router, prefix="/api/products", tags=["products"])

    @app.get("/health")
    async def health_check():
        return {"status": "healthy"}

    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
