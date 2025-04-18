Airline ticket booking and management System

This is a Django-based web application for managing airline reservations. It allows users to search for flights, book tickets, and manage their profiles.Admin
can view,modify,delete the models manually.

Features:

Flight Search: Search for flights based on origin and destination.
Booking System: Book flights and view booking success messages.
User Authentication: Login and registration for users.
Profile Management: Update user profiles.
Dynamic Suggestions: Autocomplete suggestions for cities during flight search.

Installation
Clone the repository:
git clone https://github.com/rockraghumnv/airline/
cd airline

Install dependencies:pip install -r requirements.txt(this file is being updated)

Apply migrations:
python manage.py makemigrations
python manage.py migrate

Run the development server:
Access the application at http://127.0.0.1:8000/.

Usage
Navigate to the homepage to search for flights.
Login or register to book flights.
Manage your profile from the user dashboard.
Project Structure
airline: Core Django project files.
flights: App for flight-related functionality.
profiles: App for user profile management.
users: App for user authentication.
templates: HTML templates for the application.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
