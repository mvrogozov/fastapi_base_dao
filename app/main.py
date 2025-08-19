from fastapi import FastAPI

from app.api.book import router as book_router
from app.api.person import router as person_router


app = FastAPI(
    summary='base dao'
)

app.include_router(book_router)
app.include_router(person_router)


@app.get('/')
def read_root():
    return 'Base dao root'
