import requests
from colorama import init, Fore, Back, Style
from pprint import pprint

# Headers for all requests in JSON format
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Terminal colored text setup using colorama
init()
def cprint(text):
    print(Fore.CYAN + text + Fore.RESET)
def mprint(text):
    print(Fore.MAGENTA + text + Fore.RESET)


# [=ENDPOINT REQUESTS=]

# GET /fridge
def get_fridges():
    url = "http://localhost:5000/fridge"
    r = requests.get(url, headers=headers)
    return r.json()

# Print endpoint and response
cprint("GET /fridge")
pprint(get_fridges())


# GET /fridge/<name>
def get_fridge(name):
    url = f"http://localhost:5000/fridge/{name}"
    r = requests.get(url, headers=headers)
    return r.json()

name = "Samsung Smart Fridge"

cprint("GET /fridge/<name>")
mprint(f"name: {name}")
pprint(get_fridge(name))


# GET /fridge/<name>/food
def get_fridge_food_list(name):
    url = "http://localhost:5000/fridge/" + name + "/food"
    r = requests.get(url, headers=headers)
    return r.json()

name = "Samsung Smart Fridge"

cprint("GET /fridge/<name>/food")
mprint(f"name: {name}")
pprint(get_fridge_food_list(name))


# POST /fridge/<name>/add
def add_food_to_fridge(name, food):
    url = "http://localhost:5000/fridge/" + name + "/add"
    data = {
        "name": food["name"],
        "quantity": food["quantity"],
        "color": food["color"],
        "shape": food["shape"],
        "group": food["group"]
    }
    
    r = requests.post(url, headers=headers, json=data)
    return r.json()

name = "Samsung Smart Fridge"
data = {
    "name": "orange",
    "quantity": 1,
    "color": "orange",
    "shape": "round",
    "group": "fruit"
}

cprint("POST /fridge/<name>/add")
mprint(f"name: {name}")
mprint(f"data: {data}")
pprint(add_food_to_fridge(name, data))


# PUT /fridge/<name>/eat
def eat_food_from_fridge(name, fname):
    url = f"http://localhost:5000/fridge/{name}/eat"
    r = requests.put(url, headers=headers, json={"fname": fname})
    return r.json()

name = "Samsung Smart Fridge"
fname = "banana"

cprint("PUT /fridge/<name>/eat")
mprint(f"name: {name}")
mprint(f"fname: {fname}")
pprint(eat_food_from_fridge(name, fname))


# GET /fridge/<name>/food/<fname>/quantity
def get_food_quantity(name, fname):
    url = f"http://localhost:5000/fridge/{name}/food/{fname}/quantity"
    r = requests.get(url, headers=headers)
    return r.json()

name = "Samsung Smart Fridge"
fname = "banana"

cprint("GET /fridge/<name>/food/<fname>/quantity")
mprint(f"name: {name}")
mprint(f"fname: {fname}")
pprint(get_food_quantity(name, fname))


# GET /fridge/<name>/food/<fname>/shape
def get_food_shape(name, fname):
    url = f"http://localhost:5000/fridge/{name}/food/{fname}/shape"
    r = requests.get(url, headers=headers)
    return r.json()

name = "Samsung Smart Fridge"
fname = "banana"

cprint("GET /fridge/<name>/food/<fname>/shape")
mprint(f"name: {name}")
mprint(f"fname: {fname}")
pprint(get_food_shape(name, fname))
