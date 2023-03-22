from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/') 
def uno():
  return render_template("uno_1.html")

@app.route("/uno_2", methods = ["POST"])
def uno_2():
    base = request.form["base"]
    altezza = request.form["altezza"]
    area = int(base) * int(altezza)
    return render_template("uno_2.html", base=base, altezza=altezza, area = area)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)