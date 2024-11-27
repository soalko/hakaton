import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from flask import Flask, request, render_template, redirect, make_response, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_restful import abort, Api
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/cyberdanger'
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Пример модели
class Employees(db.Model):
    __tablename__ = 'employees'
    id_employee = db.Column(db.Integer, primary_key=True, nullable=False)
    login = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.Text, nullable=False)
    second_name = db.Column(db.Text, nullable=False)
    patronymic = db.Column(db.Text, nullable=True)
    absent = db.Column(db.Boolean, nullable=False, default=True)


@app.route('/')
def index():
    # return render_template("logist.html")

    # new_emp = Employees(id_employee=1, login='soalko', password='soalko228!', first_name='Alex', second_name='Soldatov',
    #                     patronymic='Константинович', absent=False)
    # db.session.add(new_emp)
    # db.session.commit()
    # return f'User {new_emp.first_name} created'
    # # employees = Employees.query.all()
    # return '<br>'.join([f'{user.first_name} - {user.second_name}' for user in employees])
    return render_template("analysts.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    lg = request.args.get('login')
    pas = request.args.get('password')
    employee = Employees.query.filter_by(login=lg).first()
    if employee and employee.password == pas:
        login_user(employee, remember=True)
        return redirect("/")
    return render_template("login.html")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port, debug=True)
