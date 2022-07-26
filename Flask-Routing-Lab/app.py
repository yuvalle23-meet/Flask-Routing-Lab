from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Your code should be below

@app.route("/")
def function():
    return render_template("home1.html")

@app.route("/product1")
def function1():
    return render_template("product.html")

@app.route("/cart1")
def function2():
    return render_template("cart.html")

# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)

