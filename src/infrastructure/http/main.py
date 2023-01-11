# from sqlalchemy.engine import Engine
# from uvicorn import run

# if __name__ == "__main__":
#     engine: Engine = DBConnectionHandler().get_engine()
#     Base.metadata.create_all(engine=engine)
#     run(
#         app="src.infra.http.routes.server:app",
#         host="0.0.0.0",
#         port=8000,
#         reload=True,
#         log_level="debug",
#     )
