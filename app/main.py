from fastapi import FastAPI


app = FastAPI(
    summary='base dao'
)


@app.get('/')
def read_root():
    return 'Base dao root'
