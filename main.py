from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'msg': 'trip created successfully'}


@app.get('/about')
def about():
    return {'data': 'about page'}