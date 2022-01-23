from flask_app import app
from flask_app.model.user import User # importing the functions from class/model
from flask_app.controllers import users_controller

# IF RUN PROGRAM
if __name__ == "__main__":
    app.run(debug=True)
