
# Mess Finder Project

## Introduction

The Mess Finder project is a web application built with Django, aimed at helping college students and employees find nearby messes for their daily meals. Users can view mess details, menus, and even register for regular dining. Mess owners have the ability to manage customer attendance and view a list of registered customers.

## Features

- View a list of nearby messes with basic information on the home page.
- View detailed information about a specific mess, including its menu.
- Use the "Locate" button to find directions from the user's current position to the selected mess.
- Register to a mess for regular dining.
- Mess owners can manage customer attendance and view a list of registered customers.

## Installation

To set up the Mess Finder project, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/BhargavGurav/MessFinder.git
2. Navigate to the project directory:

   ```bash
   cd mess-finder
3. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate
4. Install the required packages:

   ```bash
   pip install -r requirements.txt
5. Set up the database and apply migrations:

   ```bash
   python manage.py migrate
6. Create a superuser account (for accessing the admin panel):

   ```bash
   python manage.py createsuperuser
7. Start the development server:
   
   ```bash
   python manage.py runserver
8. Open a web browser and go to http://127.0.0.1:8000 to view the application.

Usage
**Home Page:**

The home page displays a list of nearby messes along with basic information.
Users can click on a mess to view more details.
**Mess Details:**

Clicking on a mess from the home page or search results will lead to a detailed page with the mess's information, including the menu.
**Locate Button:**

The "Locate" button on the mess details page allows users to find directions from their current location to the mess.
**Registration:**

Users can register to a mess if they wish to dine there regularly.
**Admin Panel:**

The Django admin panel can be accessed at http://127.0.0.1:8000/admin to manage messes, customers, and more.
## Contributing
If you'd like to contribute to this project, please follow these steps:

Fork the repository on GitHub.
Create a new branch with a descriptive name for your feature or bug fix.
Make your changes and commit them with clear messages.
Push your branch to your fork on GitHub.
Create a pull request against the original repository.

## Contact

If you have any questions or issues, please contact guravbhargav09@gmail.com.
```




