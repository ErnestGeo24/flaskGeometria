from flask import Flask, render_template, request
import math
app = Flask(__name__)

@app.route('/') 
def quattro():
  return render_template("quattro_1.html")

@app.route("/quattro_2", methods = ["GET"])
def quattro_2():
  return render_template("quattro_2.html")

@app.route('/quattro_3')
def quattro_3():
  base = request.args.get("base")
  altezza = request.args.get("altezza")
  if id == "area":
    area = int(base) * int(altezza)
    return render_template("quattro_4.html")
  elif id == "diagonale":
    diagonale = math.sqrt(int(base) **2 + int(altezza)**2)
    return render_template("quattro_5.html", base=base, altezza=altezza, diagonale = diagonale)
  else:
    area = int(base) * int(altezza)
    diagonale = math.sqrt(int(base) **2 + int(altezza)**2)
    return render_template("quattro_6.html", base=base, altezza=altezza, area = area, diagonale = diagonale)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)