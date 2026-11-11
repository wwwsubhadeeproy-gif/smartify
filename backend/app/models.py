from datetime import date
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from enum import Enum

class Exam(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    exam_date: date
    syllabus: List["Topic"] = Relationship(back_populates="exam")

class Topic(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    exam_id: int = Field(foreign_key="exam.id")
    name: str
    difficulty: int                 # ranges from 1 (easy) to 5 (hard)
    weight: Optional[float] = None             # share of marks ranging from 0 to 1
    confidence: int = 0             # ranging from 0 (clueless) to 10 (mastered)
    est_hours: float = 2.0          # estimated time in hrs to prepare
    revisions: int = 0              # no.of revisions, always updated together with last_revised
    last_revised: Optional[date] = None   # set by the revise action, not edited directly
    exam: Optional[Exam] = Relationship(back_populates="syllabus")
    materials: List["Material"] = Relationship(back_populates="topic")
    archived: bool = False         # if True, deleted from syllabus

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    due_date: date
    priority: int = 1               # ranges from 1 (low) to 3 (high)
    finished: bool = False

class MaterialType(str, Enum):
    NOTES = "notes"
    PDF = "pdf"
    PPT = "ppt"
    BOOK = "book"
    LINK = "link"
    SYLLABUS = "syllabus"

class Material(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    type: MaterialType
    source: str                      # file path under uploads/, or a URL
    topic_id: Optional[int] = Field(default=None, foreign_key="topic.id")
    indexed: bool = False            # has RAG chunked and embedded it yet?

    topic: Optional["Topic"] = Relationship(back_populates="materials")
