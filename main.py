from flask import Flask

app = Flask(__name__)


# class Human:
#     # инициализация
#     def __init__(self, height=165, weight=76):
#         # property
#         self.height = height
#         self.weight = weight
#
#     def get_height_weight(self):
#         return f"Your height is {self.height} and your weight is {self.weight}"
#
#
# man = Human()
# print(man.height, man.weight, man.get_height_weight())
#
#
# class Rider(Human):
#     pass
#
#
# rider = Rider()
# print(rider)
@app.route("/")
def hello_world():
    return {"hello": "world"}


if "__main__" == __name__:
    app.run(host="localhost", port="8000", debug=True)
