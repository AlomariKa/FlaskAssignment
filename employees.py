from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # Import CORS
app = Flask(__name__)
CORS(app) # allowing your frontend to interact with your backend without restrictions.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'

app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db= SQLAlchemy(app)

class Employees(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100),nullable = False)
    lastname = db.Column(db.String(100),nullable = False)
    age = db.Column(db.Integer, nullable=False)
    salary = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "age": self.age,
            "salary": self.salary
        }

with app.app_context():
    db.create_all()


@app.route('/employees/',methods=["Get"])
def get_employees():
    employees =Employees.query.all()
    return jsonify([employee.to_dict() for employee in employees])

@app.route('/employees/<int:id>',methods=["Get"])
def get_employee(id):
    employee =Employees.query.get(id)
    if employee is None:
        return jsonify("No Employee Found")
    return jsonify(employee.to_dict())

@app.route('/employees/', methods=["POST"])
def create_employee():
    data = request.get_json()
    # parses the JSON data from the request body and converts it into a Python data structure
    new_employee = Employees(
        firstname=data["firstname"],
        lastname=data["lastname"],
        age=data["age"],
        salary=data["salary"]
    )
    db.session.add(new_employee)
    db.session.commit()
    new_employee_dict=new_employee.to_dict()
    return jsonify(new_employee_dict['firstname']), 201 # JSON response

@app.route('/employees/<int:id>', methods=["PUT"])
def update_employee(id):
    employee = Employees.query.get(id)
    if employee is None:
        return jsonify("No employee found"), 404

    data = request.get_json()
    # data.get("key", default_value)
    employee.firstname = data.get("firstname", employee.firstname)
    employee.lastname = data.get("lastname", employee.lastname)
    employee.age = data.get("age", employee.age)
    employee.salary = data.get("salary", employee.salary)

    db.session.commit()
    employee_dict=employee.to_dict()
    return jsonify(employee_dict['firstname'])

@app.route('/employees/<int:id>', methods=["DELETE"])
def delete_employee(id):
    employee = Employees.query.get(id)
    if employee is None:
        return jsonify("No employee found"), 404

    db.session.delete(employee)
    db.session.commit()
    employee_dict=employee.to_dict()

    return jsonify(employee_dict['firstname']), 200

if __name__ == "__main__":
    app.run(debug=True)
