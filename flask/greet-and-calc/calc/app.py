# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)


# @app.route("/add")
# def addition():
#     """add numbers a, b from the query params"""
#     a, b = int(request.args["a"]), int(request.args["b"])
#     return str(operations.add(a, b))

@app.route("/math/<operator>")
@app.route("/<operator>")
def calculate(operator):
    """evaluate numbers a, b from the query params"""
    a, b = int(request.args["a"]), int(request.args["b"])
    math_operations = {"add": operations.add, "sub": operations.sub,
                       "mult": operations.mult, "div": operations.div}
    if operator in math_operations:
        return str(math_operations.get(operator)(a, b))
    else:
        return "Not a valid operator; try 'add', 'sub', 'mult', or 'div'"
