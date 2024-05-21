from flask import Flask, render_template

app = Flask(__name__)

# Sample data for meals
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

# Home page with greetings and buttons
@app.route('/')
def home():
    return render_template('home.html')

# Page for selected meal
@app.route('/meal/<meal_type>/<item_name>')
def meal(meal_type, item_name):
    if meal_type in meals and item_name in meals[meal_type]:
        meal_data = meals[meal_type][item_name]
        return render_template('meal.html', meal_type=meal_type, name=meal_data['name'], image=meal_data['image'])
    else:
        return "Meal not found"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)