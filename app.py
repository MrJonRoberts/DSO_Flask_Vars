from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    name = "Fred"

    listOfNames  = ["Fred", "Frank", "Freddy", "Milo", "Harry"]

    p1 = { "name": "Fred",
           "age": 44,
           "bal": 45.22
           }
    p2 = {"name": "Frank",
          "age": 12,
          "bal": 4225.22
          }
    p3 = {"name": "Freddy",
          "age": 19,
          "bal": 0.22
          }
    p4 = {"name": "Milo",
          "age": 15,
          "bal": 1.22
          }
    p5 = {"name": "Harry",
          "age": 115,
          "bal": 100.22
          }

    people = [p1, p2, p3, p4, p5]

    return render_template("home.html", name=name, names=listOfNames, people=people)


if __name__ == '__main__':
    app.run()
