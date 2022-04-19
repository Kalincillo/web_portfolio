from flask import Flask

app = Flask(__name__)


@app.route('/')
def page():
    return """
<html>
    <head>
        <title>Portfolio</title>
    </head>
    <style>
        * {
            background-color: #45b1e8;
        }
    </style>
    <body>
        <h1>Webpage Portfolio<h1>
    </body>
</html>
    """

if __name__ == "__main__":
    app.run(debug = True, port = 8080)