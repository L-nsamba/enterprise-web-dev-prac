from flask import Flask, request, jsonify
import time
import base64
import io
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/analyze')
def analyze():
    #Reading different parameters from the url
    algo = request.args.get('algo')
    n = int(request.args.get('n', 100))
    steps = int(request.args.get('steps', 10))

    #Timing the algorithm
    start_time = time.time() #run_algorithm(algo, n, steps)
    total_time = time.time() - start_time

    #Compiling the graph
    fig, ax = plt.subplots()
    ax.plot([i for i in range(steps)], [i**2 for i in range(steps)])  # test data
    #Converting graph to base64
    buf = io.BytesIO() #Saves the graph into memory
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode("utf-8")

    response = {
        "algorithm": algo,
        "n": n,
        "steps": steps,
        "total_time": total_time,
        "start_time": start_time,
        "total_time": total_time,
        "path_to_graph": img_base64
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(port=3000, debug=True)