VSC:=================================

1. Create a Flask application with the following static routes:
i) / 
ii) /about
iii) /contact
Display an appropriate message on each webpage.
  
  from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Home Page"

@app.route('/about')
def about():
    return "This is About Page"

@app.route('/contact')
def contact():
    return "This is Contact Page"

if __name__ == '__main__':
    app.run(debug=True)
=====================================================================

2. Create a dynamic URL route using an integer parameter:
/student/<int:roll_no>/<name> The route should accept the student’s roll number
and name through the URL and display the student details in a structured format.

  from flask import Flask

app = Flask(__name__)

@app.route('/student/<int:roll_no>/<name>')
def student(roll_no, name):
    return f"""
    <h2>Student Details</h2>
    <p><b>Roll Number:</b> {roll_no}</p>
    <p><b>Name:</b> {name}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)

===================================================================================
3. Create a Flask application that stores an employee’s details (Employee ID, Name, Department, Basic Salary) 
in predefined variables, calculates HRA (20%), DA (12%), TA (8%), PF (10%), Gross Salary and Net Salary,
and displays a salary slip on the home page. gross_salary = basic_salary + hra + da + ta net_salary = gross_salary - pf

from flask import Flask

app = Flask(__name__)

# Employee details
employee_id = 101
name = "Payal"
department = "IT"
basic_salary = 30000

# Calculate salary components
hra = basic_salary * 20 / 100
da = basic_salary * 12 / 100
ta = basic_salary * 8 / 100
pf = basic_salary * 10 / 100

gross_salary = basic_salary + hra + da + ta
net_salary = gross_salary - pf

@app.route('/')
def home():
    return f"""
    <h2>Employee Salary Slip</h2>
    <p>Employee ID: {employee_id}</p>
    <p>Name: {name}</p>
    <p>Department: {department}</p>
    <p>Basic Salary: ₹{basic_salary}</p>
    <p>HRA (20%): ₹{hra}</p>
    <p>DA (12%): ₹{da}</p>
    <p>TA (8%): ₹{ta}</p>
    <p>PF (10%): ₹{pf}</p>
    <p>Gross Salary: ₹{gross_salary}</p>
    <p>Net Salary: ₹{net_salary}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)

=================================================================================
==================================================================================


4. Create a Flask application to develop a dynamic product information page using URL routing.
Create a dynamic URL route /product/<product_name>/<int:price>/<category> that accepts product details through the URL
and displays the product name, price, category, discount amount(10%), GST (18%), 
and final price after calculation on the webpage. Test the application by accessing the URL 
with different product values through the browser and verify the output.

  
from flask import Flask

app = Flask(__name__)

@app.route('/product/<product_name>/<int:price>/<category>')
def product(product_name, price, category):

    discount = price * 10 / 100
    price_after_discount = price - discount

    gst = price_after_discount * 18 / 100
    final_price = price_after_discount + gst

    return f"""
    <h2>Product Information</h2>
    <p><b>Product Name:</b> {product_name}</p>
    <p><b>Price:</b> ₹{price}</p>
    <p><b>Category:</b> {category}</p>
    <p><b>Discount (10%):</b> ₹{discount}</p>
    <p><b>GST (18%):</b> ₹{gst}</p>
    <p><b>Final Price:</b> ₹{final_price}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)

===============================================================================
===============================================================================
5. Create a Flask application with the following files: ● base.html ● home.html ● employees.html ● department.html Create employee data
and use Jinja2 loops to display the records. Use conditional statements to categorize employees
as Fresher, Experienced, or Senior based on experience. 
Use template inheritance and create a CSS file in static/css. Verify the application in the browser.

app.py ->...........
from flask import Flask, render_template

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Payal", "department": "IT", "experience": 1},
    {"id": 2, "name": "Rahul", "department": "HR", "experience": 3},
    {"id": 3, "name": "Sneha", "department": "Finance", "experience": 7}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/employees')
def employee_list():
    return render_template('employees.html', employees=employees)

@app.route('/department')
def department():
    return render_template('department.html')

if __name__ == '__main__':
    app.run(debug=True)

templates/base.html->..........
<!DOCTYPE html>
<html>
<head>
    <title>Employee Management</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>

    <h1>Employee Management System</h1>

    <nav>
        <a href="/">Home</a>
        <a href="/employees">Employees</a>
        <a href="/department">Department</a>
    </nav>

    {% block content %}
    {% endblock %}

</body>
</html>

templates/home.html->...................
{% extends 'base.html' %}

{% block content %}

<h2>Home Page</h2>
<p>Welcome to Employee Management System</p>

{% endblock %}

templates/employees.html->................
{% extends 'base.html' %}

{% block content %}

<h2>Employee List</h2>

{% for emp in employees %}

<p>
    ID: {{ emp.id }} <br>
    Name: {{ emp.name }} <br>
    Department: {{ emp.department }} <br>
    Experience: {{ emp.experience }} years <br>

    {% if emp.experience < 2 %}
        Category: Fresher
    {% elif emp.experience < 5 %}
        Category: Experienced
    {% else %}
        Category: Senior
    {% endif %}
</p>

<hr>

{% endfor %}

{% endblock %}

template department.html->.................
      {% extends 'base.html' %}

{% block content %}

<h2>Department Page</h2>

<p>IT Department</p>
<p>HR Department</p>
<p>Finance Department</p>

{% endblock %}

static/css/style.css->...............    
      body {
    font-family: Arial;
    margin: 30px;
}

h1 {
    text-align: center;
}

nav {
    text-align: center;
    margin: 20px;
}

nav a {
    margin: 15px;
    text-decoration: none;
}

================================================================================================================
      =====================================================================================
      
      6. Display Student Information using Jinja2 ,Create a Flask application with the following templates: base.html, home.html, student html .
Create student data containing name, roll number, and course in app.py. 
Pass the data to student.html using Jinja2 variables and display the student information. 
Use template inheritance and create a CSS file in the static/CSS folder. Verify the output in the browser.

1. app.py......................
from flask import Flask, render_template

app = Flask(__name__)

student = {
    "name": "Payal",
    "roll_no": 101,
    "course": "B.Sc. Computer Science"
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/student')
def student_info():
    return render_template('student.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)

2. templates/base.html.......................................
<!DOCTYPE html>
<html>
<head>
    <title>Student Information</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>

    <h1>Student Information System</h1>

    <nav>
        <a href="/">Home</a>
        <a href="/student">Student</a>
    </nav>

    {% block content %}
    {% endblock %}

</body>
</html>

3. templates/home.html......................................
{% extends 'base.html' %}

{% block content %}

<h2>Home Page</h2>
<p>Welcome to Student Information System</p>

{% endblock %}

4. templates/student.html..........................................
{% extends 'base.html' %}

{% block content %}

<h2>Student Details</h2>

<p>Name: {{ student.name }}</p>
<p>Roll Number: {{ student.roll_no }}</p>
<p>Course: {{ student.course }}</p>

{% endblock %}

5. static/css/style.css.........................................
body {
    font-family: Arial;
    margin: 30px;
}

h1 {
    text-align: center;
}

nav {
    text-align: center;
    margin: 20px;
}

nav a {
    margin: 15px;
    text-decoration: none;
}

=====================================================================================================
7. Display HTML Template using Flask ,Create a Flask application with the following structure: templates/home.
html Create a home.html template and display a ‘ welcome’ message using the render_template() function.
Verify the output in the browser.

project/
│
├── app.py
│
└── templates/
    └── home.html

  
1️⃣ app.py.............................
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
  
2️⃣ templates/home.html.............................
<!DOCTYPE html>
<html>
<head>
    <title>Home Page</title>
</head>
<body>

    <h1>Welcome to Flask Application</h1>

</body>
</html>

===========================================================================================
========================================================

8. Display Course List using Jinja2 Loop, Create a Flask application with the following templates: base.html, home.html,
courses.html, Create a list of five courses in app.py. Use a Jinja2 for loop to display the courses in courses.html.
Use templateinheritance and create a CSS file in the static/CSS folder. Verify the output in the browser.

project/
│
├── app.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   └── courses.html
│
└── static/
    └── css/
        └── style.css

  
1️⃣ app.py................................
from flask import Flask, render_template

app = Flask(__name__)

courses = [
    "Python",
    "Java",
    "Web Technology",
    "Data Science",
    "Database Management"
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/courses')
def course_list():
    return render_template('courses.html', courses=courses)

if __name__ == '__main__':
    app.run(debug=True)


2️⃣ templates/base.html.............................
<!DOCTYPE html>
<html>
<head>
    <title>Course List</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>

    <h1>Course Management System</h1>

    <nav>
        <a href="/">Home</a>
        <a href="/courses">Courses</a>
    </nav>

    {% block content %}
    {% endblock %}

</body>
</html>

3️⃣ templates/home.html........................
{% extends 'base.html' %}

{% block content %}

<h2>Home Page</h2>
<p>Welcome to Course Management System</p>

{% endblock %}

4️⃣ templates/courses.html.........................


{% extends 'base.html' %}

{% block content %}

<h2>Available Courses</h2>

<ul>
    {% for course in courses %}
        <li>{{ course }}</li>
    {% endfor %}
</ul>

{% endblock %}

  
5️⃣ static/css/style.css...............................

body {
    font-family: Arial;
    margin: 30px;
}

h1 {
    text-align: center;
}

nav {
    text-align: center;
    margin: 20px;
}

nav a {
    margin: 15px;
    text-decoration: none;
}

li {
    margin: 10px;
}
======================================================================================================
=====================================================================

9. Student Result using Jinja2 Conditional Statements ,Create a Flask application with the following templates:base.html,home.html,result.html .
Create student name and percentage in app.py. Use Jinja2 conditional statements to display the result as Distinction, First Class, Second Class, Pass,
or Fail according to the percentage. Use template inheritance and create a CSS file in the static/CSS folder. Verify the output in the browser.


project/
│
├── app.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   └── result.html
│
└── static/
    └── css/
        └── style.css

  
1️⃣ app.py...............................
  
from flask import Flask, render_template

app = Flask(__name__)

student_name = "Payal"
percentage = 78

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result')
def result():
    return render_template(
        'result.html',
        name=student_name,
        percentage=percentage
    )

if __name__ == '__main__':
    app.run(debug=True)
  
2️⃣ templates/base.html..................................

<!DOCTYPE html>
<html>
<head>
    <title>Student Result</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>

    <h1>Student Result System</h1>

    <nav>
        <a href="/">Home</a>
        <a href="/result">Result</a>
    </nav>

    {% block content %}
    {% endblock %}

</body>
</html>

3️⃣ templates/home.html....................................................

{% extends 'base.html' %}

{% block content %}

<h2>Home Page</h2>
<p>Welcome to Student Result System</p>

{% endblock %}

4️⃣ templates/result.html.........................................

{% extends 'base.html' %}

{% block content %}

<h2>Student Result</h2>

<p>Name: {{ name }}</p>
<p>Percentage: {{ percentage }}%</p>

{% if percentage >= 75 %}
    <p>Result: Distinction</p>

{% elif percentage >= 60 %}
    <p>Result: First Class</p>

{% elif percentage >= 50 %}
    <p>Result: Second Class</p>

{% elif percentage >= 40 %}
    <p>Result: Pass</p>

{% else %}
    <p>Result: Fail</p>
{% endif %}

{% endblock %}

5️⃣ static/css/style.css.........................................

body {
    font-family: Arial;
    margin: 30px;
}

h1 {
    text-align: center;
}

nav {
    text-align: center;
    margin: 20px;
}

nav a {
    margin: 15px;
    text-decoration: none;
}

====================================================================================
======================================================================

10. Apply CSS Styling using Static Folder . Create a Flask application with the following structure: templates/home.
html and static/CSS/style.css .Create a home.html template and apply CSS styling using the style.css file in the static/CSS folder. 
Apply simple styling to the heading, paragraph, background, and text alignment. Verify the output in the browser.

project/
│
├── app.py
│
├── templates/
│   └── home.html
│
└── static/
    └── CSS/
        └── style.css
  
1️⃣ app.py.............................
  
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
  
2️⃣ templates/home.html............................

<!DOCTYPE html>
<html>
<head>
    <title>Home Page</title>

    <link rel="stylesheet"
          href="{{ url_for('static', filename='CSS/style.css') }}">
</head>

<body>

    <h1>Welcome to Flask</h1>

    <p>This is a Flask application with CSS styling.</p>

</body>
</html>

3️⃣ static/CSS/style.css................................

body {
    background-color: lightblue;
    text-align: center;
}

h1 {
    color: blue;
    font-size: 35px;
}

p {
    color: black;
    font-size: 20px;
}

=================================================================================
=============================================================================
11.
Product List using Jinja2 Loop and Conditional Statements Create a Flask
application with the following templates:base.html,home.html,products.html .Create
product data containing product name, price, and availability in app.py. Use a Jinja2
for loop to display the products and conditional statements to display Available or
Out of Stock. Use template inheritance and create a CSS file in the static/CSS folder.
Verify the output in the browser.

  project/
│
├── app.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   └── products.html
│
└── static/
    └── CSS/
        └── style.css

  
1️⃣ app.py................................
  
from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"name": "Laptop", "price": 50000, "available": True},
    {"name": "Mobile", "price": 20000, "available": True},
    {"name": "Headphones", "price": 2000, "available": False},
    {"name": "Keyboard", "price": 1000, "available": True}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def product_list():
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
  
2️⃣ templates/base.html...............................

<!DOCTYPE html>
<html>
<head>
    <title>Product List</title>
    <link rel="stylesheet"
          href="{{ url_for('static', filename='CSS/style.css') }}">
</head>
<body>

    <h1>Product Management System</h1>

    <nav>
        <a href="/">Home</a>
        <a href="/products">Products</a>
    </nav>

    {% block content %}
    {% endblock %}

</body>
</html>

3️⃣ templates/home.html.................................

{% extends 'base.html' %}

{% block content %}

<h2>Home Page</h2>
<p>Welcome to Product Management System</p>

{% endblock %}

4️⃣ templates/products.html.........................................

{% extends 'base.html' %}

{% block content %}

<h2>Product List</h2>

{% for product in products %}

<p>
    <b>Product Name:</b> {{ product.name }} <br>
    <b>Price:</b> ₹{{ product.price }} <br>

    {% if product.available %}
        <b>Status:</b> Available
    {% else %}
        <b>Status:</b> Out of Stock
    {% endif %}
</p>

<hr>

{% endfor %}

{% endblock %}
 
5️⃣ static/CSS/style.css................................

body {
    font-family: Arial;
    margin: 30px;
    text-align: center;
}

h1 {
    color: blue;
}

nav {
    margin: 20px;
}

nav a {
    margin: 15px;
    text-decoration: none;
}

==============================================================================================
================================================================================

12. Create a Flask Employee Information Form containing Employee ID, Employee Name,
Department, and Designation. Accept the form data using the POST method
and display the submitted information on the web page.
............................
  from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    emp_id = request.form['emp_id']
    name = request.form['name']
    department = request.form['department']
    designation = request.form['designation']

    return f"""
    <h2>Employee Information</h2>
    <p>Employee ID: {emp_id}</p>
    <p>Employee Name: {name}</p>
    <p>Department: {department}</p>
    <p>Designation: {designation}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)

.................................
templates/form.html...................................
  
<!DOCTYPE html>
<html>
<head>
    <title>Employee Information Form</title>
</head>
<body>

<h2>Employee Information Form</h2>

<form action="/submit" method="POST">

    Employee ID:
    <input type="text" name="emp_id"><br><br>

    Employee Name:
    <input type="text" name="name"><br><br>

    Department:
    <input type="text" name="department"><br><br>

    Designation:
    <input type="text" name="designation"><br><br>

    <input type="submit" value="Submit">

</form>

</body>
</html>

=======================================================================================
==========================================================

13 Create a Flask Contact Form containing Name, Email, Subject, and Message. 
Check whether all fields are filled and display an appropriate flash message.

project/
│
├── app.py
│
└── templates/
    └── contact.html

    app.py.................................
    

from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    if name and email and subject and message:
        flash("Contact form submitted successfully!")
    else:
        flash("Please fill all fields.")

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

templates/contact.html................................

  <!DOCTYPE html>
<html>
<head>
    <title>Contact Form</title>
</head>
<body>

<h2>Contact Form</h2>

{% with messages = get_flashed_messages() %}
    {% for message in messages %}
        <p>{{ message }}</p>
    {% endfor %}
{% endwith %}

<form action="/submit" method="POST">

    Name:
    <input type="text" name="name"><br><br>

    Email:
    <input type="email" name="email"><br><br>

    Subject:
    <input type="text" name="subject"><br><br>

    Message:
    <textarea name="message"></textarea><br><br>

    <input type="submit" value="Submit">

</form>

</body>
</html>  
=========================================================================================================
=====================================================

14.
Create a Flask Event Registration Form containing Participant Name, Mobile
Number, and Event Name. Provide three event options and display the submitted
information using a flash message

project/
│
├── app.py
│
└── templates/
    └── event.html

    app.py.............................

from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def event():
    return render_template('event.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    mobile = request.form['mobile']
    event_name = request.form['event_name']

    flash(f"Registration Successful! Name: {name}, Mobile: {mobile}, Event: {event_name}")

    return render_template('event.html')

if __name__ == '__main__':
    app.run(debug=True)


templates/event.html..................

<!DOCTYPE html>
<html>
<head>
    <title>Event Registration</title>
</head>
<body>

<h2>Event Registration Form</h2>

{% with messages = get_flashed_messages() %}
    {% for message in messages %}
        <p>{{ message }}</p>
    {% endfor %}
{% endwith %}

<form action="/register" method="POST">

    Participant Name:
    <input type="text" name="name"><br><br>

    Mobile Number:
    <input type="text" name="mobile"><br><br>

    Event Name:
    <select name="event_name">
        <option value="Coding Competition">Coding Competition</option>
        <option value="Quiz Competition">Quiz Competition</option>
        <option value="Project Exhibition">Project Exhibition</option>
    </select>
    <br><br>

    <input type="submit" value="Register">

</form>

</body>
</html>


=======================================================================
==================================================================


15. Create a Flask Electricity Bill Form containing Consumer Name, Consumer Number, and Units Consumed.
Calculate the electricity bill according to different unit slabs and display the total bill.


project/
│
├── app.py
│
└── templates/
    └── bill.html


app.py.....................................

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def bill():
    return render_template('bill.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    name = request.form['name']
    number = request.form['number']
    units = int(request.form['units'])

    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = (100 * 2) + ((units - 100) * 3)
    elif units <= 300:
        bill = (100 * 2) + (100 * 3) + ((units - 200) * 4)
    else:
        bill = (100 * 2) + (100 * 3) + (100 * 4) + ((units - 300) * 5)

    return f"""
    <h2>Electricity Bill</h2>
    <p>Consumer Name: {name}</p>
    <p>Consumer Number: {number}</p>
    <p>Units Consumed: {units}</p>
    <p>Total Bill: ₹{bill}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)


templates/bill.html.......................................

    <!DOCTYPE html>
<html>
<head>
    <title>Electricity Bill</title>
</head>
<body>

<h2>Electricity Bill Form</h2>

<form action="/calculate" method="POST">

    Consumer Name:
    <input type="text" name="name"><br><br>

    Consumer Number:
    <input type="text" name="number"><br><br>

    Units Consumed:
    <input type="number" name="units"><br><br>

    <input type="submit" value="Calculate Bill">

</form>

</body>
</html>

==============================================================================
======================================================================

16. Create a Flask Age Calculator Form that accepts a person’s Name and Date of Birth. 
Calculate and display the person's age on the result page.
Display an appropriate flash message if the required input is missing.

project/
│
├── app.py
│
└── templates/
    └── age.html

app.py.......................................

from flask import Flask, render_template, request, flash
from datetime import date

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def age():
    return render_template('age.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    name = request.form['name']
    dob = request.form['dob']

    if not name or not dob:
        flash("Please enter Name and Date of Birth.")
        return render_template('age.html')

    dob = date.fromisoformat(dob)
    today = date.today()

    age = today.year - dob.year

    if (today.month, today.day) < (dob.month, dob.day):
        age = age - 1

    return f"""
    <h2>Age Calculator Result</h2>
    <p>Name: {name}</p>
    <p>Age: {age} years</p>
    """

if __name__ == '__main__':
    app.run(debug=True)


 templates/age.html........................

<!DOCTYPE html>
<html>
<head>
    <title>Age Calculator</title>
</head>
<body>

<h2>Age Calculator Form</h2>

{% with messages = get_flashed_messages() %}
    {% for message in messages %}
        <p>{{ message }}</p>
    {% endfor %}
{% endwith %}

<form action="/calculate" method="POST">

    Name:
    <input type="text" name="name"><br><br>

    Date of Birth:
    <input type="date" name="dob"><br><br>

    <input type="submit" value="Calculate Age">

</form>

</body>
</html>


================================
==============================================================================================

16.
Create a Flask Age Calculator Form that accepts a person’s Name and Date of Birth.
Calculate and display the person's age on the result page. Display an appropriate
flash message if the required input is missing.

project/
│
├── app.py
│
└── templates/
    └── age.html

    app.py............................
    
from flask import Flask, render_template, request, flash
from datetime import date

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def home():
    return render_template('age.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    name = request.form['name']
    dob = request.form['dob']

    if not name or not dob:
        flash("Please enter Name and Date of Birth.")
        return render_template('age.html')

    dob = date.fromisoformat(dob)
    today = date.today()

    age = today.year - dob.year

    if (today.month, today.day) < (dob.month, dob.day):
        age = age - 1

    return f"""
    <h2>Age Calculator Result</h2>
    <p>Name: {name}</p>
    <p>Age: {age} years</p>
    """

if __name__ == '__main__':
    app.run(debug=True)

    templates/age.html....................................

    <!DOCTYPE html>
<html>
<head>
    <title>Age Calculator</title>
</head>
<body>

<h2>Age Calculator Form</h2>

{% with messages = get_flashed_messages() %}
    {% for message in messages %}
        <p>{{ message }}</p>
    {% endfor %}
{% endwith %}

<form action="/calculate" method="POST">

    Name:
    <input type="text" name="name"><br><br>

    Date of Birth:
    <input type="date" name="dob"><br><br>

    <input type="submit" value="Calculate Age">

</form>

</body>
</html>



=================================================================+==
===================================================================================
17. Create a Flask Temperature Conversion Form that accepts a temperature value and allows the user to
select Celsius to Fahrenheit or Fahrenheit to Celsius. Perform the selected conversion and display the result.

project/
│
├── app.py
│
└── templates/
    └── temperature.html

    app.py...............................
    
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('temperature.html')

@app.route('/convert', methods=['POST'])
def convert():
    temperature = float(request.form['temperature'])
    conversion = request.form['conversion']

    if conversion == 'CtoF':
        result = (temperature * 9/5) + 32
        message = f"{temperature} °C = {result} °F"

    else:
        result = (temperature - 32) * 5/9
        message = f"{temperature} °F = {result} °C"

    return f"""
    <h2>Temperature Conversion Result</h2>
    <p>{message}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)

    templates/temperature.html..........................................

    <!DOCTYPE html>
<html>
<head>
    <title>Temperature Conversion</title>
</head>
<body>

<h2>Temperature Conversion Form</h2>

<form action="/convert" method="POST">

    Temperature:
    <input type="number" step="any" name="temperature">

    <br><br>

    Conversion:
    <select name="conversion">
        <option value="CtoF">Celsius to Fahrenheit</option>
        <option value="FtoC">Fahrenheit to Celsius</option>
    </select>

    <br><br>

    <input type="submit" value="Convert">

</form>

</body>
</html>


+===========================================================================================
============================================

18. Create a Flask Student Attendance Form containing Student Name, Total Working Days,
and Days Present. Calculate the attendance percentage and display whether the student is Eligible or Not
Eligible based on a minimum attendance requirement of 75%. Display appropriate flash messages

app.py....................................

from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def home():
    return render_template('attendance.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    name = request.form['name']
    total_days = int(request.form['total_days'])
    present_days = int(request.form['present_days'])

    percentage = (present_days / total_days) * 100

    if percentage >= 75:
        flash(f"{name}: Eligible. Attendance = {percentage:.2f}%")
    else:
        flash(f"{name}: Not Eligible. Attendance = {percentage:.2f}%")

    return render_template('attendance.html')

if __name__ == '__main__':
    app.run(debug=True)


    
templates/attendance.html......................................

<!DOCTYPE html>
<html>
<head>
    <title>Student Attendance</title>
</head>
<body>

<h2>Student Attendance Form</h2>

{% with messages = get_flashed_messages() %}
    {% for message in messages %}
        <p>{{ message }}</p>
    {% endfor %}
{% endwith %}

<form action="/calculate" method="POST">

    Student Name:
    <input type="text" name="name"><br><br>

    Total Working Days:
    <input type="number" name="total_days"><br><br>

    Days Present:
    <input type="number" name="present_days"><br><br>

    <input type="submit" value="Calculate Attendance">

</form>

</body>
</html>


============================================================================================
=========================================


19 Create a Flask Restaurant Order Form containing Customer Name, Food Item,Quantity, and Price.
Calculate the subtotal, apply a 5% service charge, add 18% GST,and display the final bill.
Validate the input fields and display appropriate flash messages for invalid input.

app.py.............................


from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def home():
    return render_template('order.html')

@app.route('/order', methods=['POST'])
def order():
    name = request.form['name']
    food = request.form['food']
    quantity = request.form['quantity']
    price = request.form['price']

    if not name or not food or not quantity or not price:
        flash("Please fill all fields.")
        return render_template('order.html')

    quantity = int(quantity)
    price = float(price)

    if quantity <= 0 or price <= 0:
        flash("Quantity and Price must be greater than 0.")
        return render_template('order.html')

    subtotal = quantity * price
    service_charge = subtotal * 5 / 100
    gst = (subtotal + service_charge) * 18 / 100
    final_bill = subtotal + service_charge + gst

    return f"""
    <h2>Restaurant Bill</h2>
    <p>Customer Name: {name}</p>
    <p>Food Item: {food}</p>
    <p>Quantity: {quantity}</p>
    <p>Price: ₹{price}</p>
    <p>Subtotal: ₹{subtotal}</p>
    <p>Service Charge (5%): ₹{service_charge}</p>
    <p>GST (18%): ₹{gst}</p>
    <p>Final Bill: ₹{final_bill}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)


    
templates/order.html.....................................

<!DOCTYPE html>
<html>
<head>
    <title>Restaurant Order</title>
</head>
<body>

<h2>Restaurant Order Form</h2>

{% with messages = get_flashed_messages() %}
    {% for message in messages %}
        <p>{{ message }}</p>
    {% endfor %}
{% endwith %}

<form action="/order" method="POST">

    Customer Name:
    <input type="text" name="name"><br><br>

    Food Item:
    <input type="text" name="food"><br><br>

    Quantity:
    <input type="number" name="quantity"><br><br>

    Price:
    <input type="number" step="any" name="price"><br><br>

    <input type="submit" value="Calculate Bill">

</form>

</body>
</html>

=================================================================================
========================================================================================

20. Develop a Flask-based Student Management System using SQLite that creates a database with a student table containing id,
name, age, and course fields, allows users to insert new student records, 
and displays all student records on the home page.

project/
│
├── app.py
└── templates/
    └── index.html

    app.py..............................
    
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def create_database():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            course TEXT
        )
    ''')

    conn.commit()
    conn.close()

create_database()

@app.route('/')
def home():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM student')
    students = cursor.fetchall()

    conn.close()

    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    id = request.form['id']
    name = request.form['name']
    age = request.form['age']
    course = request.form['course']

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO student VALUES (?, ?, ?, ?)',
        (id, name, age, course)
    )

    conn.commit()
    conn.close()

    return home()

if __name__ == '__main__':
    app.run(debug=True)

    
templates/index.html.......................................

<!DOCTYPE html>
<html>
<head>
    <title>Student Management System</title>
</head>
<body>

<h2>Student Management System</h2>

<form action="/add" method="POST">

    ID:
    <input type="number" name="id"><br><br>

    Name:
    <input type="text" name="name"><br><br>

    Age:
    <input type="number" name="age"><br><br>

    Course:
    <input type="text" name="course"><br><br>

    <input type="submit" value="Add Student">

</form>

<h2>Student Records</h2>

<table border="1">
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Age</th>
        <th>Course</th>
    </tr>

    {% for student in students %}
    <tr>
        <td>{{ student[0] }}</td>
        <td>{{ student[1] }}</td>
        <td>{{ student[2] }}</td>
        <td>{{ student[3] }}</td>
    </tr>
    {% endfor %}

</table>

</body>
</html>

=============================================================================================
=====================================================================

21. Develop a complete Flask-based Student Management System using SQLite. 
Implement all CRUD operations: ● Create ● Read ● Update ● Delete Display all records
in an HTML table and verify each database operation on the web browser.

project/
│
├── app.py
└── templates/
    ├── index.html
    └── edit.html


    app.py..................................

    from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def create_database():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            course TEXT
        )
    ''')

    conn.commit()
    conn.close()


create_database()


# READ
@app.route('/')
def home():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM student')
    students = cursor.fetchall()

    conn.close()

    return render_template('index.html', students=students)


# CREATE
@app.route('/add', methods=['POST'])
def add():
    id = request.form['id']
    name = request.form['name']
    age = request.form['age']
    course = request.form['course']

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO student VALUES (?, ?, ?, ?)',
        (id, name, age, course)
    )

    conn.commit()
    conn.close()

    return redirect('/')


# UPDATE
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        course = request.form['course']

        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()

        cursor.execute(
            'UPDATE student SET name=?, age=?, course=? WHERE id=?',
            (name, age, course, id)
        )

        conn.commit()
        conn.close()

        return redirect('/')

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM student WHERE id=?', (id,))
    student = cursor.fetchone()

    conn.close()

    return render_template('edit.html', student=student)


# DELETE
@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM student WHERE id=?', (id,))

    conn.commit()
    conn.close()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

templates/index.html..................................................

<!DOCTYPE html>
<html>
<head>
    <title>Student Management System</title>
</head>
<body>

<h2>Student Management System</h2>

<h3>Add Student</h3>

<form action="/add" method="POST">

    ID:
    <input type="number" name="id"><br><br>

    Name:
    <input type="text" name="name"><br><br>

    Age:
    <input type="number" name="age"><br><br>

    Course:
    <input type="text" name="course"><br><br>

    <input type="submit" value="Add Student">

</form>

<h3>Student Records</h3>

<table border="1">
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Age</th>
        <th>Course</th>
        <th>Actions</th>
    </tr>

    {% for student in students %}
    <tr>
        <td>{{ student[0] }}</td>
        <td>{{ student[1] }}</td>
        <td>{{ student[2] }}</td>
        <td>{{ student[3] }}</td>

        <td>
            <a href="/update/{{ student[0] }}">Update</a>
            |
            <a href="/delete/{{ student[0] }}">Delete</a>
        </td>
    </tr>
    {% endfor %}

</table>

</body>
</html>

templates/edit.html...............................

<!DOCTYPE html>
<html>
<head>
    <title>Update Student</title>
</head>
<body>

<h2>Update Student</h2>

<form action="/update/{{ student[0] }}" method="POST">

    Name:
    <input type="text" name="name" value="{{ student[1] }}"><br><br>

    Age:
    <input type="number" name="age" value="{{ student[2] }}"><br><br>

    Course:
    <input type="text" name="course" value="{{ student[3] }}"><br><br>

    <input type="submit" value="Update Student">

</form>

</body>
</html>

==================================================================================================

    
