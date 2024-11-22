import os

from calc import sqrt

from flask import (
    Flask,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)

app = Flask(__name__)


@app.route("/")
def index():
    print("Request for index page received")
    return render_template("index.html")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )

@app.route("/calc", methods=["POST"])
def calc():
    name = str(sqrt(float(request.form.get("name"))))

    if name :
        print("Request for calc page received with name=%s" % name)
        return render_template("calc.html", name=name)
    else:
        print(
            "Request for calc page received with no name or blank name -- redirecting"
        )
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
