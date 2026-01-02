

from .database import get_db_connection

def get_all_employees():
    conn = get_db_connection()
    employees = conn.execute("SELECT * FROM employees").fetchall()
    conn.close()
    return employees

def add_employee(name, department, position):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO employees (name, department, position) VALUES (?, ?, ?)",
        (name, department, position)
    )
    conn.commit()
    conn.close()



def get_employee_by_id(id):
    conn = get_db_connection()
    emp = conn.execute(
        "SELECT * FROM employees WHERE id = ?",
        (id,)
    ).fetchone()
    conn.close()
    return emp


def update_employee(id, name, department, position):
    conn = get_db_connection()
    conn.execute(
        "UPDATE employees SET name=?, department=?, position=? WHERE id=?",
        (name, department, position, id)
    )
    conn.commit()
    conn.close()


def delete_employee(id):
    conn = get_db_connection()
    conn.execute(
        "DELETE FROM employees WHERE id=?",
        (id,)
    )
    conn.commit()
    conn.close()
