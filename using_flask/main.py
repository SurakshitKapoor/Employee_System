
from app import create_app

app = create_app()


# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     print("this is home(/) page!")
#     return """
#     <h1> Home Page </h1>
#     <p> <i> Details of employees mentioned below! </i> <p>
#     """

if __name__=="__main__":
    print("starting the app from main.py")
    app.run(debug=True)