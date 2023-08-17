from flask import Flask, request, jsonify
import util
app=Flask(__name__)

@app.route('/get_location_name', methods=['GET'])
def get_location_name():
    response=jsonify({'location':util.get_location()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response












if(__name__=="__main__"):
    util.load_artifacts()
    app.run(debug=True)