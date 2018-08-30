from rrd import app
from flask import render_template

@app.route("/thirdparty/grafana")
def grafana():
    return render_template("thirdparty/grafana.html", **locals())