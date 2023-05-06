# import fast api
from fastapi import FastAPI

# other imports as required
from typing import Optional
from pydantic import BaseModel
import uvicorn

# create instance of fast api
app = FastAPI()


# basic -
# function name can be anything.
# route is dertermined by the path inside the decorator
#
# if a variable is present in both path and function parameter, then it is considered as path parameter
# if a varaibel is present only in function parameter, then it is considered as query parameter



# in this function, all paramters are query parameters
# if default value is not set for query parameters, then it will throw error if query is not passed
# alternatively, if you dont want to set default value for a query, use Optional keyword and set value to None
@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}



@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}



# in this function, id is path parameter
@app.get('/blog/{id}')
def show(id: int):
    # return blog with id == id
    return {'data': id}



@app.get('/blog/{id}/comments')
def comments(id):
    # return comments of the blog with id == id
    return {'data': {'1', '2'}}



class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]



@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"Blog is created with title as {blog.title}"}



# without below main function, to start server -
# cmnd: uvicorn main:app --reload   (reload flag will refresh whenever we save code)
# with main, to start server - 
# cmnd: python main.py    (python3 if your default is not python3)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)