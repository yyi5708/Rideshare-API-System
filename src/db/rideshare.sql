DROP TABLE IF EXISTS Drivers CASCADE;
DROP TABLE IF EXISTS Riders CASCADE;
DROP TABLE IF EXISTS Rides CASCADE;
DROP TABLE IF EXISTS Reviews CASCADE;

CREATE TABLE Drivers (
driver_id SERIAL PRIMARY KEY NOT NULL,
name TEXT NOT NULL,
average_rating DECIMAL(2,1) NOT NULL,
special_instructions TEXT NOT NULL,
car_make_model TEXT NOT NULL,
license_number TEXT NOT NULL,
years_as_driver INTEGER NOT NULL,
joining_date TIMESTAMP NOT NULL,
coordinates POINT NOT NULL,
zipcode TEXT NOT NULL );

CREATE TABLE Riders (
rider_id SERIAL PRIMARY KEY NOT NULL,
name TEXT NOT NULL,
average_rating DECIMAL(2,1) NOT NULL,
special_instructions TEXT NOT NULL,
credit_card_number TEXT NOT NULL,
used_for TEXT NOT NULL,
years_as_rider INTEGER NOT NULL,
joining_date TIMESTAMP NOT NULL,
coordinates POINT NOT NULL,
zipcode TEXT NOT NULL );

CREATE TABLE Rides (
ride_id SERIAL PRIMARY KEY NOT NULL,
driver_id INTEGER NOT NULL REFERENCES Drivers(driver_id) ON DELETE CASCADE,
rider_id INTEGER NOT NULL REFERENCES Riders(rider_id) ON DELETE CASCADE,
start_point TEXT NOT NULL,
destination TEXT NOT NULL,
special_instructions TEXT NOT NULL,
time_info TIMESTAMP NOT NULL,
driver_review_text TEXT NOT NULL,
rider_review_text TEXT NOT NULL,
done BOOLEAN NOT NULL );
        
CREATE TABLE Reviews (
review_id SERIAL PRIMARY KEY NOT NULL,
ride_id INTEGER NOT NULL REFERENCES Rides(ride_id) ON DELETE CASCADE,
reviewer_id INTEGER NOT NULL REFERENCES Riders(rider_id) ON DELETE CASCADE,
review_text TEXT NOT NULL,
done BOOLEAN NOT NULL );