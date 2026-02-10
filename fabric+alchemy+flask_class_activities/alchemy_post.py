from flask import Flask, request, jsonify
from sqlalchemy.orm import sessionmaker
from alchemy_activity import engine, AlgoAnalysis

app = Flask(__name__)
Session = sessionmaker(bind=engine)

@app.route("/save_analysis", methods=["POST"])
def save_analysis():
    data = request.json
    session = Session()

    analysis = AlgoAnalysis(
        algo = data["algo"],
        items = data["items"],
        steps = data["steps"],
        start_time = data["start_time"],
        end_time = data["end_time"],
        total_time_ms = data["total_time_ms"],
        time_complexity = data["time_complexity"],
        path_to_graph = data.get("path_to_graph")
    )
    session.add(analysis)
    session.commit()

    return jsonify({"status": "success", "id":analysis.id}), 201

if __name__ == "__main__":
    app.run()