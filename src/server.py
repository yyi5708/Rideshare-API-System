from flask import Flask, jsonify
from flask_restful import Api
from api.management import *

app = Flask(__name__)
api = Api(app)

api.add_resource(Init, '/manage/init')
api.add_resource(Version, '/manage/version')

@app.route('/drivers', methods=['POST'])
def create_driver_1():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'data is not found'}), 404
    driver = create_driver(data.get('name'), data.get('average_rating'), data.get('special_instructions'),
                              data.get('car_make_model'), data.get('license_number'), data.get('years_as_driver'),
                              data.get('joining_date'), data.get('coordinates'), data.get('zipcode'))
    return jsonify({'driver_id': driver}), 200

@app.route('/riders', methods=['POST'])
def create_rider_2():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'data is not found'}), 404
    rider = create_rider(data.get('name'), data.get('average_rating'), data.get('special_instructions'),
                            data.get('credit_card_number'), data.get('used_for'), data.get('years_as_rider'),
                            data.get('joining_date'), data.get('coordinates'), data.get('zipcode'))
    return jsonify({'rider_id': rider}), 200

@app.route('/rides', methods=['POST'])
def create_ride_3():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'data is not found'}), 404
    ride = create_ride(data.get('driver_id'), data.get('rider_id'), data.get('start_point'), data.get('destination'),
                          data.get('special_instructions'), data.get('time_info'), data.get('driver_review_text'),
                          data.get('rider_review_text'), data.get('done'))
    return jsonify({'ride_id': ride}), 200

@app.route('/reviews', methods=['POST'])
def create_review_4():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'data is not found'}), 404
    review = create_review(data.get('ride_id'), data.get('reviewer_id'), data.get('review_text'), data.get('done'))
    return jsonify({'review_id': review}), 200

@app.route('/', methods=['GET'])
def read_home_5():
    return jsonify({'message': 'rideshare'}), 200

@app.route('/drivers', methods=['GET'])
def read_drivers_6():
    return jsonify(read_drivers()), 200

@app.route('/riders', methods=['GET'])
def read_riders_7():
    return jsonify(read_riders()), 200

@app.route('/rides', methods=['GET'])
def read_rides_8():
    return jsonify(read_rides()), 200

@app.route('/reviews', methods=['GET'])
def read_reviews_9():
    return jsonify(read_reviews()), 200

@app.route('/driver/<int:id>', methods=['GET'])
def read_driver_10(id):
    driver = read_driver(id)
    if driver:
        return jsonify(driver), 200
    else:
        return jsonify({'message': 'driver is not found'}), 404

@app.route('/rider/<int:id>', methods=['GET'])
def read_rider_11(id):
    rider = read_rider(id)
    if rider:
        return jsonify(rider), 200
    else:
        return jsonify({'message': 'rider is not found'}), 404
        
@app.route('/ride/<int:id>', methods=['GET'])
def read_ride_12(id):
    ride = read_ride(id)
    if ride:
        return jsonify(ride), 200
    else:
        return jsonify({'message': 'ride is not found'}), 404

@app.route('/review/<int:id>', methods=['GET'])
def read_review_13(id):
    review = read_review(id)
    if review:
        return jsonify(review), 200
    else:
        return jsonify({'message': 'review is not found'}), 404

@app.route('/driver/<int:driver_id>', methods=['PUT'])
def update_driver_14(driver_id):
    data = request.get_json()
    if not data:
        return jsonify({'message': 'data is not found'}), 404
    name = data.get('name')
    average_rating = data.get('average_rating')
    special_instructions = data.get('special_instructions')
    car_make_model = data.get('car_make_model')
    license_number = data.get('license_number')
    years_as_driver = data.get('years_as_driver')
    joining_date = data.get('joining_date')
    coordinates = data.get('coordinates')
    zipcode = data.get('zipcode')
    driver = update_driver(driver_id, name, average_rating, special_instructions, car_make_model, license_number,
                           years_as_driver, joining_date, coordinates, zipcode)
    if driver:
        return jsonify({'message': 'driver is updated'}), 200
    else:
        return jsonify({'message': 'driver is not updated'}), 404

@app.route('/rider/<int:rider_id>', methods=['PUT'])
def update_rider_15(rider_id):
    data = request.get_json()
    if not data:
        return jsonify({'message': 'data is not found'}), 404
    name = data.get('name')
    average_rating = data.get('average_rating')
    special_instructions = data.get('special_instructions')
    credit_card_number = data.get('credit_card_number')
    used_for = data.get('used_for')
    years_as_rider = data.get('years_as_rider')
    joining_date = data.get('joining_date')
    coordinates = data.get('coordinates')
    zipcode = data.get('zipcode')
    rider = update_rider(rider_id, name, average_rating, special_instructions, credit_card_number, used_for,
                          years_as_rider, joining_date, coordinates, zipcode)
    if rider:
        return jsonify({'message': 'rider is updated'}), 200
    else:
        return jsonify({'message': 'rider is not updated'}), 404

@app.route('/ride/<int:ride_id>', methods=['PUT'])
def update_ride_16(ride_id):
    data = request.get_json()
    if not data:
        return jsonify({'message': 'data is not found'}), 404
    driver_id = data.get('driver_id')
    rider_id = data.get('rider_id')
    start_point = data.get('start_point')
    destination = data.get('destination')
    special_instructions = data.get('special_instructions')
    time_info = data.get('time_info')
    driver_review_text = data.get('driver_review_text')
    rider_review_text = data.get('rider_review_text')
    done = data.get('done')
    review = update_ride(ride_id, driver_id, rider_id, start_point, destination, special_instructions,
                         time_info, driver_review_text, rider_review_text, done)
    if review:
        return jsonify({'message': 'ride is updated'}), 200
    else:
        return jsonify({'message': 'ride is not updated'}), 404

@app.route('/review/<int:review_id>', methods=['PUT'])
def update_review_17(review_id):
    data = request.get_json()
    if not data:
        return jsonify({'message': 'data is not found'}), 404
    ride_id = data.get('ride_id')
    reviewer_id = data.get('reviewer_id')
    review_text = data.get('review_text')
    done = data.get('done')
    review = update_review(review_id, ride_id, reviewer_id, review_text, done)
    if review:
        return jsonify({'message': 'review is updated'}), 200
    else:
        return jsonify({'message': 'review is not updated'}), 404

@app.route('/driver/<int:id>', methods=['DELETE'])
def delete_driver_18(id):
    driver = read_driver(id)
    if not driver:
        return jsonify({'message': 'driver is not found'}), 404
    delete_driver(id)
    return jsonify({'message': 'driver is deleted'}), 200

@app.route('/rider/<int:id>', methods=['DELETE'])
def delete_rider_19(id):
    rider = read_rider(id)
    if not rider:
        return jsonify({'message': 'rider is not found'}), 404
    delete_rider(id)
    return jsonify({'message': 'rider is deleted'}), 200

@app.route('/ride/<int:id>', methods=['DELETE'])
def delete_ride_20(id):
    ride = read_ride(id)
    if not ride:
        return jsonify({'message': 'ride is not found'}), 404
    delete_ride(id)
    return jsonify({'message': 'ride is deleted'}), 200

@app.route('/review/<int:id>', methods=['DELETE'])
def delete_review_21(id):
    review = read_review(id)
    if not review:
        return jsonify({'message': 'review is not found'}), 404
    delete_review(id)
    return jsonify({'message': 'review is deleted'}), 200

if __name__ == '__main__':
    rebuildTables()
    app.run(debug=True)