INSERT INTO Drivers (driver_id, name, average_rating, special_instructions, car_make_model, license_number, years_as_driver, joining_date, coordinates, zipcode)
VALUES
  (1, 'Driver 1', 4.5, 'No Smoking', 'Toyota Camry', 'ABC123', 3, '2022-01-01', POINT(40.7128, -74.0060), '10001'),
  (2, 'Driver 2', 4.2, 'No Food', 'Honda Accord', 'XYZ456', 5, '2021-06-15', POINT(34.0522, -118.2437), '20002'),
  (3, 'Driver 3', 4.7, 'No Drink', 'Ford Fusion', 'DEF789', 2, '2023-03-10', POINT(51.5074, -0.1278), '30003'),
  (4, 'Driver 4', 4.0, 'No Pets', 'Chevrolet Cruze', 'GHI101', 4, '2020-12-01', POINT(45.4215, -75.6981), '40004'),
  (5, 'Driver 5', 4.9, 'Buckle Up', 'Tesla Model 3', 'JKL202', 1, '2023-01-20', POINT(48.8566, 2.3522), '50005');

INSERT INTO Riders (rider_id, name, average_rating, special_instructions, credit_card_number, used_for, years_as_rider, joining_date, coordinates, zipcode)
VALUES
  (1, 'Rider 1', 4.3, 'Drive Fast', '1111-2222-3333-4444', 'Work Transportation', '3', '2022-02-05', POINT(40.7306, -73.9352), '10001'),
  (2, 'Rider 2', 4.8, 'Drive Slow', '5555-6666-7777-8888', 'Work Transportation', '5', '2021-10-12', POINT(34.0522, -118.2437), '20002'),
  (3, 'Rider 3', 4.2, 'Drive Fast', '9999-0000-1111-2222', 'Work Transportation', '2', '2023-04-20', POINT(51.5074, -0.1278), '30003'),
  (4, 'Rider 4', 4.6, 'Drive Slow', '3333-4444-5555-6666', 'Work Transportation', '4', '2020-11-30', POINT(45.4215, -75.6981), '40004'),
  (5, 'Rider 5', 4.4, 'Drive Fast', '7777-8888-9999-0000', 'Work Transportation', '1', '2023-02-10', POINT(48.8566, 2.3522), '50005');

INSERT INTO Rides (ride_id, driver_id, rider_id, start_point, destination, special_instructions, time_info, driver_review_text, rider_review_text, done)
VALUES
  (1, 1, 1, 'Point A', 'Point B', 'No Special Instructions', '2022-02-10 08:00:00', 'No Driver Review', 'No Rider Review', False),
  (2, 2, 2, 'Point C', 'Point D', 'No Special Instructions', '2021-10-15 12:30:00', 'No Driver Review', 'No Rider Review', False),
  (3, 3, 3, 'Point E', 'Point F', 'No Special Instructions', '2023-04-25 15:45:00', 'No Driver Review', 'No Rider Review', False),
  (4, 4, 4, 'Point G', 'Point H', 'No Special Instructions', '2020-12-05 18:00:00', 'No Driver Review', 'No Rider Review', False),
  (5, 5, 5, 'Point I', 'Point J', 'No Special Instructions', '2023-02-15 10:00:00', 'No Driver Review', 'No Rider Review', False);

INSERT INTO Reviews (review_id, ride_id, reviewer_id, review_text, done)
VALUES
  (1, 1, 1, 'Great ride!', False),
  (2, 2, 2, 'Excellent service.', False),
  (3, 3, 3, 'Smooth ride experience.', False),
  (4, 4, 4, 'Friendly driver.', False),
  (5, 5, 5, 'Pleasant journey.', False);