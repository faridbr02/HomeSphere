from flask import Flask, request, jsonify

app = Flask(__name__)

home_data = {
    "Sensors": {
        "id": 0,
        "data": {
            "Temperature": 36.5,
            "Humidity": 68,
            "Movement": 0,
            "Air Quality": 0,
            "Fire": 0,
        }
    },
    "Home devices": {
        "id": 1,
        "data": {
            "Wifi": False,
            "Garage": False,
            "Camera": False,
            "Outside light": False,
        }
    },
    "Living Room": {
        "id": 2,
        "data": {
            "Light1": False,
            "Light2": False,
            "SmartTv": False,
            "Air Conditioner": False,
            "Window": False,
            "Curtain": False,
        }
    },
    "Kitchen": {
        "id": 3,
        "data": {
            "Light": False,
            "Window": False,
            "Dishwasher": False,
            "Rangehood": False,
        }
    },
    "Stairs": {
        "id": 4,
        "data": {
            "Light1": False,
            "Light2": False,
        }
    },
    "Bedroom": {
        "id": 5,
        "data": {
            "SmartTv": False,
            "Window": False,
            "Gaming Setup": False,
            "DoorLock": False,
            "Light": False,
        }
    },
}

@app.route('/data', methods=['GET', 'POST'])
def get_home_data():
    if request.method == 'GET':
        if home_data:
            return jsonify(home_data)
        else:
            return 'Nothing to Show', 404
    elif request.method == 'POST':
        # Here you can handle data updates (if needed)
        return 'Update functionality not implemented', 501




@app.route('/data/<int:id>', methods=['GET'])
def get_data_by_id(id):
    category = None
    for key, value in home_data.items():
        if value['id'] == id:
            category = key
            break
    
    if category is not None:
        return jsonify({category: home_data[category]})
    else:
        return f'Category with ID {id} not found', 404



@app.route('/data/id=<int:id>', methods=['GET', 'PUT'])
def get_or_update_data_by_id(id):
    if request.method == 'GET':
        category = None
        for key, value in home_data.items():
            if value['id'] == id:
                category = key
                break
        
        if category is not None:
            return jsonify({category: home_data[category]})
        else:
            return f'Category with ID {id} not found', 404
    
    elif request.method == 'PUT':
        req_data = request.get_json()
        category = None
        for key, value in home_data.items():
            if value['id'] == id:
                category = key
                home_data[key]['data'].update(req_data.get('data', {}))
                return jsonify({category: home_data[category]})
        
        if category is None:
            return f'Category with ID {id} not found', 404




if __name__ == '__main__':
    app.run(debug=True)
    
    
