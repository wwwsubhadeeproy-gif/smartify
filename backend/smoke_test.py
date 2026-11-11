from sqlmodel import SQLModel, create_engine
from app import models

engine = create_engine("sqlite://")
SQLModel.metadata.create_all(engine)
models.Topic(exam_id=1, name="x", difficulty=1)
print("ok")