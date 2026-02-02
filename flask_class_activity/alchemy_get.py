from flask import Flask, request
from sqlalchemy.orm import sessionmaker
from alchemy_post import jsonify
from alchemy_activity import engine, AlgoAnalysis

app = Flask(__name__)
Session = sessionmaker(bind=engine)

@app.route("/retrieve_analysis", methods=["GET"])
def retrieve_analysis():
    analysis_id = request.args.get("id")
    session = Session()
    analysis = session.query(AlgoAnalysis).get(analysis_id)

    if not analysis:
        return jsonify({"error": "Analysis not found"}), 404
    
    return jsonify({
        "id": analysis.id,
        "algo": analysis.algo,
        "items": analysis.items,
        "steps": analysis.steps,
        "start_time": analysis.start_time,
        "end_time": analysis.end_time,
        "total_time_ms": analysis.total_time_ms,
        "time_complexity": analysis.time_complexity,
        "path_to_graph": analysis.path_to_graph
    })

if __name__ == "__main__":
    app.run()