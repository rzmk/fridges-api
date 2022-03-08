from flask import Flask, render_template, jsonify, request

"""
FRIDGE API

fridge is an object that stores food:
- List of foods
- Name
- Price
food is an object with certain properties:
- Quantity
- Color
- Shape
- Name

[=SAMPLES=]

Sample fridge:
{
    "name": "Samsung Smart Fridge",
    "price": "10000.0",
    "food": []
}

Sample food:
{
    "name": "banana",
    "quantity": 3,
    "color": "yellow",
    "shape": "crescent",
    "group": "fruit"
}

[=ENDPOINTS=]

GET /fridge
- Return a list of all fridges we own

GET /fridge/<name>
- Returns a fridge with the given name

GET /fridge/<name>/food
- Returns a list of food that fridge <name> stores

PUT /fridge/<name>/eat
- data:{fname:"fname", quantity:"q"}
- Remove "q" amount of food "fname" from fridge "name"

POST /fridge/<name>/add
- data:{fname:"fname", (details...), quantity:"q"}
- Add new type of food to fridge

GET /fridge/<name>/food/<fname>/quantity
- Returns the quantity of food "fname" in fridge "name"

GET /fridge/<name>/food/<fname>/shape
- Returns the shape of food "fname" in fridge "name"

"""

# Initial data

fridges = [
    {
        "name": "Samsung Smart Fridge",
        "price": "10000.0",
        "food": [
            {
                "name": "banana",
                "quantity": 3,
                "color": "yellow",
                "shape": "crescent",
                "group": "fruit"
            },
            {
                "name": "apple",
                "quantity": 2,
                "color": "red",
                "shape": "round",
                "group": "fruit"
            },
            {
                "name": "milk",
                "quantity": 1,
                "color": "white",
                "shape": "round",
                "group": "drink"
            }
        ]
    },
    {
        "name": "LG Smart Fridge",
        "price": "5000.0",
        "food": [
            {
                "name": "banana",
                "quantity": 2,
                "color": "yellow",
                "shape": "crescent",
                "group": "fruit"
            },
            {
                "name": "watermelon",
                "quantity": 1,
                "color": "green",
                "shape": "round",
                "group": "fruit"
            },
            {
                "name": "water",
                "quantity": 1,
                "color": "blue",
                "shape": "round",
                "group": "drink"
            }
        ]
    }
]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# GET /fridge
# - Return a list of all fridges we own
@app.route("/fridge", methods=["GET"])
def get_fridges():
    return jsonify({ "fridges": fridges })

# GET /fridge/<name>
# - Returns a fridge with the given name
@app.route("/fridge/<string:name>", methods=["GET"])
def get_fridge(name):
    for fridge in fridges:
        if fridge["name"] == name:
            return jsonify(fridge)
    return jsonify({ "message": "Fridge not found" })

# GET /fridge/<string:name>/food
# - Returns a list of food that fridge <name> stores
@app.route("/fridge/<string:name>/food", methods=["GET"])
def get_fridge_food_list(name):
    for fridge in fridges:
        if fridge["name"] == name:
            return jsonify({ "food": fridge["food"] })
    return jsonify({ "message": "Fridge not found" })

# PUT /fridge/<string:name>/eat
# - data:{fname:"fname", quantity:"q"}
# - Remove "q" amount of food "fname" from fridge "name"
@app.route("/fridge/<string:name>/eat", methods=["PUT"])
def eat_food_from_fridge(name):
    request_data = request.get_json()
    for fridge in fridges:
        if fridge["name"] == name:
            for food in fridge["food"]:
                if food["name"] == request_data["fname"]:
                    food["quantity"] = food["quantity"] - 1
                    return jsonify({ "message": "Successfully removed food" })
    return jsonify({ "message": "Fridge not found" })

# POST /fridge/<string:name>/add
# - data:{fname:"fname", (details...), quantity:"q"}
# - Add new type of food to fridge
@app.route("/fridge/<string:name>/add", methods=["POST"])
def add_item_to_fridge(name):
    request_data = request.get_json()
    for fridge in fridges:
        if fridge["name"] == name:
            if request_data["name"] in [food["name"] for food in fridge["food"]]:
                return jsonify({ "message": "Food already in fridge" })
            new_food = {
                "name": request_data["name"],
                "quantity": request_data["quantity"],
                "color": request_data["color"],
                "shape": request_data["shape"],
                "group": request_data["group"]
            }
            fridge["food"].append(new_food)
            return jsonify({ "message": "Food added to fridge" })
    return jsonify({ "message": "Fridge not found" })

# GET /fridge/<string:name>/food/<string:fname>/quantity
# - Returns the quantity of food "fname" in fridge "name"
@app.route("/fridge/<string:name>/food/<string:fname>/quantity", methods=["GET"])
def get_food_quantity(name, fname):
    for fridge in fridges:
        if fridge["name"] == name:
            for food in fridge["food"]:
                if food["name"] == fname:
                    return jsonify({ "quantity": food["quantity"] })
    return jsonify({ "message": "Fridge not found" })

# GET /fridge/<string:name>/food/<string:fname>/shape
# - Returns the shape of food "fname" in fridge "name"
@app.route("/fridge/<string:name>/food/<string:fname>/shape", methods=["GET"])
def get_food_shape(name, fname):
    for fridge in fridges:
        if fridge["name"] == name:
            for food in fridge["food"]:
                if food["name"] == fname:
                    return jsonify({ "shape": food["shape"] })
    return jsonify({ "message": "Fridge not found" })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
