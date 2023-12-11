from flask import Flask, request, redirect
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

services = {}
scores = {'blue_score': 0, 'blue_two_score' : 0, 'red_score': 0}

@app.route("/")
def landing_page():
    return redirect('/display_scores')

@app.route("/display_scores", methods=['GET'])
def display_services():
    print(f"receives {request} FROM {request.host}\n\n")
    content = {'services': services, 'scores' : scores}
    return content


@app.route("/manual_input")
def manual_input():
    return redirect('/manual_input')

@app.route("/increment_blue_score", methods=['POST'])
def increment_blue_score():
    try:
        print(f"Received POST request FROM {request.host}\n\n")

        blue_score = int(request.form['blue_score'])
        scores['blue_score'] = str(blue_score)

        return {"Success": True}
    except Exception as e:
        print(f"Error: {e}")
        return {"Success": False}

@app.route("/increment_blue_two_score", methods=['POST'])
def increment_blue_two_score():
    try:
        print(f"Received POST request FROM {request.host}\n\n")

        blue_two_score = int(request.form['blue_two_score'])
        scores['blue_two_score'] = str(blue_two_score)

        # print(scores['blue_two_score'])
        return {"Success": True}
    except Exception as e:
        print(f"Error: {e}")
        return {"Success": False}

@app.route("/increment_red_score", methods=['POST'])
def increment_red_score():
    try:
        print(f"Received POST request FROM {request.host}\n\n")

        red_score = int(request.form['red_score'])
        scores['red_score'] = str(red_score)

        # print(scores['red_score'])
        return {"Success": True}
    except Exception as e:
        print(f"Error: {e}")
        return {"Success": False}

@app.route("/update_scores", methods=['POST'])
def update_scores():
    print({request})
    try:
        print(f"receives {request} FROM {request.host}\n\n")
        blue_score = request.form['blue_score']
        blue_two_score = request.form['blue_two_score']
        red_score = request.form['red_score']
        scores['blue_score'] = str(blue_score)
        scores['blue_two_score'] = str(blue_two_score)
        scores['red_score'] = str(red_score)
        for key in services.keys():
            print(services[key])
        print(scores)
        
        return {"Success":True}
    except Exception:
        return {"Success":False}


@app.route("/update_services", methods=['POST'])
def update_services():
    try:
        print(f"Received {request} FROM {request.host}\n\n")

        host = request.form['host']
        service = request.form['service']
        status = request.form['status']
        score = request.form['value']
        team = request.form['team']

        if host in services.keys():
            if service in services[host].keys():
                services[host][service] = [status, team]
            else:
                services[host][service] = [status, team]
        else:
            services[host] = {service : [status, team]}
        return {'Success': True}
    except Exception:
        return {'Success' : False}

