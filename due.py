from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/') 
def due():
  return render_template("due_1.html")

@app.route("/due_2", methods = ["GET"])
def due_2():
    base = request.args.get("base")
    altezza = request.args.get("altezza")
    area = int(base) * int(altezza)
    return render_template("due_2.html", base = base, altezza = altezza, area = area)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)