from fastapi import FastAPI
from fastapi.responses import RedirectResponse
def setup_global_events(app: FastAPI):
    # Redirect
    @app.get("/", include_in_schema=False)
    async def root():
        return RedirectResponse(url="/docs")

    # Set global events
    async def startup_event(): pass

    # execute global events
    @app.on_event("startup")
    async def on_startup():
        await startup_event()

    @app.on_event("shutdown")
    async def shutdown(): pass