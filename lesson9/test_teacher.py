import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session


DATABASE_URL = "postgresql://postgres:342507@localhost:5432/QA"
engine = create_engine(DATABASE_URL)
Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teacher'
    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)
    group_id = Column(Integer, nullable=False)


@pytest.fixture(scope="function", autouse=True)
def setup_database():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


def test_add_teacher():
    with Session(engine) as session:
        new_teacher = Teacher(email="test_add@example.com", group_id=1)
        session.add(new_teacher)
        session.commit()

        added_teacher = session.query(Teacher).filter_by(
            email="test_add@example.com").first()
        assert added_teacher is not None
        assert added_teacher.group_id == 1


def test_update_teacher():
    with Session(engine) as session:
        new_teacher = Teacher(email="test_update@example.com", group_id=1)
        session.add(new_teacher)

        teacher_to_update = session.query(Teacher).filter_by(
            email="test_update@example.com").first()
        teacher_to_update.email = "updated@example.com"
        session.commit()

        updated_teacher = session.query(Teacher).filter_by(
            email="updated@example.com").first()
        assert updated_teacher is not None


def test_delete_teacher():
    with Session(engine) as session:
        new_teacher = Teacher(email="test_delete@example.com", group_id=1)
        session.add(new_teacher)
        session.commit()

        teacher_to_delete = session.query(Teacher).filter_by(
            email="test_delete@example.com").first()
        session.delete(teacher_to_delete)
        session.commit()

        deleted_teacher = session.query(Teacher).filter_by(
            email="test_delete@example.com").first()
        assert deleted_teacher is None
