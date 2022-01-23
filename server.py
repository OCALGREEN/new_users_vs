from flask import Flask, render_template, redirect, request
from user import User # importing the functions from class/model

app = Flask(__name__)
app.secret_key = "secret secret key"

# HOME PAGE
@app.route("/")
def index():
    users = User.get_all() # calling the get_all() function from the class/model to output the information onto the html
    print(users) # prints info onto the terminal for trouble shooting
    return render_template("index.html", users = users)


# CREATE PAGE ADD NEW USER
@app.route("/create")
def create():
    return render_template("create.html")

# WILL REDIRECT TO HOME PAGE WITH NEW USER CREATED
@app.route("/create/new_user", methods=["POST"])
def create_new_user():
    data = {
        "fname": request.form["fname"], # we make a dictionary from our request.form coming fromt the template
        "lname": request.form["lname"], # the keys in the data need to line up exactly with the variables in our query string
        "nemail": request.form["nemail"],
    }
    User.save(data) # we pass the data dictionary into the save data method from the class
    return redirect("/")


# WILL SHOW THE SELECTED PERSONS INFORMATION
@app.route("/show/<int:user_id>")
def show(user_id):
    return render_template("show.html", this_user = User.get_one({"id": user_id}))


# EDIT PAGE
@app.route("/edit/<int:user_id>")
def edit(user_id):
    return render_template("edit.html", this_user = User.get_one({"id": user_id}))

# EDIT PAGE REDIRECT
@app.route("/edit/<int:user_id>/update", methods = ["POST"])
def edit_user(user_id):
    updated_data = {
        **request.form, 
        "id": user_id
    }
    User.update(updated_data)
    return redirect("/")

# IF RUN PROGRAM
if __name__ == "__main__":
    app.run(debug=True)
