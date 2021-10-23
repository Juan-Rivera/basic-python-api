# Basic Flask-RESTful API

This project shows one of the possible ways to implement RESTful API server using CRUD operations in Flask.


Project structure:
```
.
├── README.md
├── app.py
├── requirements.txt

```

* app.py - flask application initialization.
* requirements - holds all packages needed for project.


## Running 

1. Clone repository.
2. pip install requirements.txt
3. Run app.py 

## Usage
### Recipes endpoint
GET localhost:5000/recipes

RESPONSE
```json
{
    "data": [
        {
            "description": "This is a lovely egg salad recipe.",
            "id": 1,
            "name": "Egg Salad"
        },
        {
            "description": "This is a lovely tomato pasta recipe.",
            "id": 2,
            "name": "Tomato Pasta"
        },
    ]
}
```
GET localhost:5000/recipes/2
```json
{
    "description": "This is a lovely tomato pasta recipe.",
    "id": 2,
    "name": "Tomato Pasta"
}
```
POST localhost:5000/recipes

REQUEST
```json
{
    "name": "Cheese Pizza",
    "description": "This is a lovely cheese pizza recipe."
}
```
RESPONSE
```json
{
    "description": "This is a lovely cheese pizza recipe.",
    "id": 3,
    "name": "Cheese Pizza"
}
```
PUT localhost:5000/recipes/3

REQUEST
```json
{
    "name": "Lovely Cheese Pizza",
    "description": "This is a lovely cheese pizza recipe."
}
```
RESPONSE
```json
{
    "description": "This is a lovely cheese pizza recipe.",
    "id": 3,
    "name": "Lovely Cheese Pizza"
}
```
DELETE localhost:5000/recipes/3

RESPONSE
```json
{
  "message": "recipe succesfully deleted"
}
```
