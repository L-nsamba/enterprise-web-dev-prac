from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import  Column, Integer, String, BigInteger
from sqlalchemy.orm import declarative_base

engine = create_engine("mysql+pymysql://leon_workbench:leon%40alu.1@localhost:3306/hbnb_db")
connection = engine.connect()
Base = declarative_base()

class AlgoAnalysis(Base):
    __tablename__ = "algo_analysis"

    id = Column(Integer, primary_key=True, autoincrement=True)
    algo = Column(String(50), nullable=False)
    items = Column(Integer, nullable=False)
    steps = Column(Integer, nullable=False)
    start_time = Column(BigInteger, nullable=False)
    end_time = Column(BigInteger, nullable=False)
    total_time_ms = Column(Integer, nullable=False)
    time_complexity = Column(String(20), nullable=False)
    path_to_graph = Column(String(225), nullable=True)

Base.metadata.create_all(engine)
print("Connected successfully")