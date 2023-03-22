from flask import Flask, render_template, request
import math
app = Flask(__name__)

@app.route('/') 
def tre():
  return render_template("tre_1.html")

@app.route("/tre_2", methods = ["POST"])
def tre_2():
    base = request.form["base"]
    altezza = request.form["altezza"]
    if id == "area":
      area = float(base) * float(altezza)
      return render_template("quattro_3.html", base=base, altezza=altezza, area = area)
    elif id == "diagonale":
      diagonale = math.sqrt(float(base) **2 + float(altezza)**2)
      return render_template("quattro_4.html", base=base, altezza=altezza, diagonale = diagonale)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)