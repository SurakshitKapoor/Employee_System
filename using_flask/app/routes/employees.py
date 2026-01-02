

from flask import Blueprint, render_template, request, redirect, url_for
from app.models import (
    get_all_employees,
    get_employee_by_id,
    add_employee,
    update_employee,
    delete_employee
)

employees_bp = Blueprint("employees", __name__)

@employees_bp.route("/")
def home():
    employees = get_all_employees()
    return render_template("home.html", employees=employees)


@employees_bp.route("/employees/new", methods=["GET", "POST"])
def create_employee():
    if request.method == "POST":
        add_employee(
            request.form["name"],
            request.form["department"],
            request.form["position"]
        )
        return redirect(url_for("employees.home"))

    return render_template("add_employee.html")


@employees_bp.route("/employees/<int:id>/edit", methods=["GET", "POST"])
def edit_employee(id):
    employee = get_employee_by_id(id)

    if request.method == "POST":
        update_employee(
            id,
            request.form["name"],
            request.form["department"],
            request.form["position"]
        )
        return redirect(url_for("employees.home"))

    return render_template("edit_employee.html", employee=employee)


@employees_bp.route("/employees/<int:id>/delete", methods=["POST"])
def remove_employee(id):
    delete_employee(id)
    return redirect(url_for("employees.home"))
