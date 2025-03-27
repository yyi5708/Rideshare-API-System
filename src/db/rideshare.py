from db.swen344_db_utils import *

def rebuildTables():
    exec_sql_file("src/db/rideshare.sql")
    exec_sql_file("src/db/rideshare_data.sql")

def create_driver(name, average_rating, special_instructions, car_make_model, license_number, years_as_driver, joining_date, coordinates, zipcode):
    sql = """
    INSERT INTO Drivers (name, average_rating, special_instructions, car_make_model, license_number, years_as_driver, joining_date, coordinates, zipcode)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    RETURNING driver_id;
    """
    return exec_commit(sql, (name, average_rating, special_instructions, car_make_model, license_number, years_as_driver, joining_date, coordinates, zipcode))

def create_rider(name, average_rating, special_instructions, credit_card_number, used_for, years_as_rider, joining_date, coordinates, zipcode):
    sql = """
    INSERT INTO Riders (name, average_rating, special_instructions, credit_card_number, used_for, years_as_rider, joining_date, coordinates, zipcode)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    RETURNING rider_id;
    """
    return exec_commit(sql, (name, average_rating, special_instructions, credit_card_number, used_for, years_as_rider, joining_date, coordinates, zipcode))

def create_ride(driver_id, rider_id, start_point, destination, special_instructions, time_info, driver_review_text, rider_review_text, done):
    sql = """
    INSERT INTO Rides (driver_id, rider_id, start_point, destination, special_instructions, time_info, driver_review_text, rider_review_text, done)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    RETURNING ride_id;
    """
    return exec_commit(sql, (driver_id, rider_id, start_point, destination, special_instructions, time_info, driver_review_text, rider_review_text, done))

def create_review(ride_id, reviewer_id, review_text, done):
    sql = """
    INSERT INTO Reviews (ride_id, reviewer_id, review_text, done)
    VALUES (%s, %s, %s, %s)
    RETURNING review_id;
    """
    return exec_commit(sql, (ride_id, reviewer_id, review_text, done))

def read_drivers():
    sql = """
    SELECT * FROM Drivers;
    """
    return exec_get_all(sql)

def read_riders():
    sql = """
    SELECT * FROM Riders;
    """
    return exec_get_all(sql)

def read_rides():
    sql = """
    SELECT * FROM Rides;
    """
    return exec_get_all(sql)

def read_reviews():
    sql = """
    SELECT * FROM Reviews;
    """
    return exec_get_all(sql)

def read_driver(driver_id):
    sql = """
    SELECT * FROM Drivers WHERE driver_id = %s;
    """
    return exec_get_one(sql, (driver_id,))

def read_rider(rider_id):
    sql = """
    SELECT * FROM Riders WHERE rider_id = %s;
    """
    return exec_get_one(sql, (rider_id,))

def read_ride(ride_id):
    sql = """
    SELECT * FROM Rides WHERE ride_id = %s;
    """
    return exec_get_one(sql, (ride_id,))

def read_review(review_id):
    sql = """
    SELECT * FROM Reviews WHERE review_id = %s;
    """
    return exec_get_one(sql, (review_id,))

def update_driver(driver_id, name, average_rating, special_instructions, car_make_model, license_number, years_as_driver, joining_date, coordinates, zipcode):
    sql = """
    UPDATE Drivers
    SET name = %s, average_rating = %s, special_instructions = %s, car_make_model = %s, license_number = %s, years_as_driver = %s, joining_date = %s, coordinates = %s, zipcode = %s
    WHERE driver_id = %s;
    """
    return exec_commit(sql, (name, average_rating, special_instructions, car_make_model, license_number, years_as_driver, joining_date, coordinates, zipcode, driver_id))

def update_rider(rider_id, name, average_rating, special_instructions, credit_card_number, used_for, years_as_rider, joining_date, coordinates, zipcode):
    sql = """
    UPDATE Riders
    SET name = %s, average_rating = %s, special_instructions = %s, credit_card_number = %s, used_for = %s, years_as_rider = %s, joining_date = %s, coordinates = %s, zipcode = %s
    WHERE rider_id = %s;
    """
    return exec_commit(sql, (name, average_rating, special_instructions, credit_card_number, used_for, years_as_rider, joining_date, coordinates, zipcode, rider_id))

def update_ride(ride_id, driver_id, rider_id, start_point, destination, special_instructions, time_info, driver_review_text, rider_review_text, done):
    sql = """
    UPDATE Rides
    SET driver_id = %s, rider_id = %s, start_point = %s, destination = %s, special_instructions = %s, time_info = %s, driver_review_text = %s, rider_review_text = %s, done = %s
    WHERE ride_id = %s;
    """
    return exec_commit(sql, (driver_id, rider_id, start_point, destination, special_instructions, time_info, driver_review_text, rider_review_text, done, ride_id))

def update_review(review_id, ride_id, reviewer_id, review_text, done):
    sql = """
    UPDATE Reviews
    SET ride_id = %s, reviewer_id = %s, review_text = %s, done = %s
    WHERE review_id = %s;
    """
    return exec_commit(sql, (ride_id, reviewer_id, review_text, done, review_id))

def delete_driver(driver_id):
    sql = """
    DELETE FROM Drivers WHERE driver_id = %s;
    """
    return exec_commit(sql, (driver_id,))

def delete_rider(rider_id):
    sql = """
    DELETE FROM Riders WHERE rider_id = %s;
    """
    return exec_commit(sql, (rider_id,))

def delete_ride(ride_id):
    sql = """
    DELETE FROM Rides WHERE ride_id = %s;
    """
    return exec_commit(sql, (ride_id,))

def delete_review(review_id):
    sql = """
    DELETE FROM Reviews WHERE review_id = %s;
    """
    return exec_commit(sql, (review_id,))