# Flask-Menu-Web-App



This project is a simple web application built using Flask, designed to showcase different meals for breakfast and dinner. It features a user-friendly interface with buttons that direct users to detailed pages for each meal, including images and names. The project was executed on an SSH browser from Google Cloud Platform (GCP), demonstrating deployment in a cloud environment.

Project Description

 Features

1. Home Page: 
   - Displays a greeting and buttons for meal selection.
   - Allows users to navigate to detailed meal pages.

2. Meal Pages:
   - Separate pages for each meal item showing the meal's name and image.
   - Dynamic URL routing based on meal type (e.g., Breakfast, Dinner) and item name.

Data Structure

  - Meals Dictionary: Stores information about available meals categorized by meal type (Breakfast, Dinner).
  ```python
  meals = {
      'Breakfast': {
          'Masala_Dosa': {'name': 'Masala Dosa', 'image': 'https://i.pinimg.com/736x/e8/dc/7f/e8dc7f0b59b8602ba30621dee3c6291c.jpg'},
          'Poha': {'name': 'Poha', 'image': 'https://www.cookwithmanali.com/wp-content/uploads/2014/08/Poha-Recipe.jpg'}
      },
      'Dinner': {
          'Butter_Chicken': {'name': 'Butter Chicken', 'image': 'https://www.licious.in/blog/wp-content/uploads/2022/02/image-1.png'},
          'Veg_Biryani': {'name': 'Veg Biryani', 'image': 'https://nishkitchen.com/wp-content/uploads/2017/11/Veg-Biryani-7B.jpg'}
      }
  }
  ```

 Flask Application

  - Route Definitions:
  - `/`: Home page displaying a greeting and buttons for meal types.
  - `/meal/<meal_type>/<item_name>`: Dynamic route for displaying specific meal details.

  -Templates:
  - `home.html`: Template for the home page.
  - `meal.html`: Template for displaying details of a selected meal.

### Running the Application on GCP

1. Set Up GCP VM:
   - Create a VM instance on Google Cloud Platform.
   - SSH into the VM instance.

2. Install Flask:
   - Ensure Flask is installed on the VM: `pip install flask`.

3. Deploy the Application:
   - Save the provided code in a file named `app.py`.
   - Create a `templates` directory with `home.html` and `meal.html` files.
   - Run the Flask application: `python app.py`.

4. Access the Application:
   - Open the web browser and navigate to the external IP address of your VM instance on port 5000.

Example Usage

- Navigate to the home page.
- Click on a meal type button (e.g., "Breakfast" or "Dinner").
- Select a specific meal to view its details.

This project demonstrates the basics of Flask routing, dynamic URL handling, and template rendering, as well as deploying a Flask application in a cloud environment using Google Cloud Platform.
