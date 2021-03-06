from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)

recipes = [
    {
        'id': 1,
        'name': 'Egg Salad',
        'description': 'This is a lovely egg salad recipe.'
    },
    {
        'id': 2,
        'name': 'Tomato Pasta',
        'description': 'This is a lovely tomato pasta recipe.'
    }
]


@app.route('/recipes', methods=['GET'])
def get_recipes():
    return jsonify({'data': recipes})


@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)
    if recipe:
        return jsonify(recipe)
    return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND


@app.route('/recipes', methods=['POST'])
def create_recipe():
    # breakdown data
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    # construct recipe object
    recipe = {
        'id': len(recipes) + 1,
        'name': name,
        'description': description
    }
    # append new recipe to the recipes list
    recipes.append(recipe)

    # return back json object of new recipe, alongside the HTTPS 201 status
    return jsonify(recipe), HTTPStatus.CREATED


@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)

    if not recipe:
        return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND

    # breakdown data
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    # inject new details
    recipe.update({
        'name': name,
        'description': description
    })

    # return back json object of updated recipe, no status code needed (default 200 OK)
    return jsonify(recipe)


@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)
    if not recipe:
        return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND
    recipes.remove(recipe)

    return jsonify(recipe, {'message': 'recipe successfully deleted'})


if __name__ == '__main__':
    app.run()
