from flask import Flask, render_template
from flask_bootstrap import Bootstrap

import redis

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    
    alerts = {}
    try:
        conn = redis.StrictRedis(host="redis", port=6379)
        
        for key in conn.scan_iter():
            alerts[key] = conn.get(key)

    except Exception as ex:
        print(ex)

    return render_template("index.html", alerts=alerts)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")