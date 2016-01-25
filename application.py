from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application-form")
def show_application_form():
    """ """

    return render_template("application-form.html")


@app.route("/application-response", methods=["POST"])
def show_application_response():
    """ """
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    salary = request.form.get('salary')
    position = request.form.get('position')

    return render_template("application-response.html", 
                           firstname = firstname,
                           lastname = lastname,
                           position = position,
                           salary = salary)


if __name__ == "__main__":
    app.run(debug=True)
