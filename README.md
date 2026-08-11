# Radiator Springs Garage Management System (GMS)

## Description

A console-based Garage Management System developed in Python using Object-Oriented Programming (OOP). The system manages different types of vehicles in Radiator Springs Garage, allowing users to add, update, search, remove, and manage garage records. It also saves all data in a JSON file so that records are preserved between program runs.

## Features

- Check in new vehicles.
- Prevent duplicate car numbers.
- View all vehicles currently in the garage.
- Update vehicle information (Tune-Up).
- Retire (remove) a vehicle.
- Search for a vehicle by car number.
- Generate a garage report including:
  - Total number of checked-in vehicles.
  - Average performance score.
  - Number of vehicles in each racing team.
- Automatic Performance Score calculation using Polymorphism:
  - Racer = (Speed × 10) + Capacity
  - Support Vehicle = (Speed × 5) + (Capacity × 5)
- Data validation using setters:
  - Positive age.
  - Positive speed.
  - Positive capacity.
- Automatic saving and loading of garage data using a JSON file.

## OOP Concepts Used

- Classes and Objects
- Encapsulation (Getters and Setters)
- Inheritance
- Polymorphism
- File Handling (JSON)

## Technologies

- Python 3
- JSON
