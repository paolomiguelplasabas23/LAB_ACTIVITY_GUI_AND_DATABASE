from database import database
from model import Student
from repository import StudentRepository

class StudentService:
    def __init__(self, database: database):
        self.repository = StudentRepository(database)

    def add_student(self, student: Student) -> Student:
        return self.repository.add(student)

    def get_students(self) -> list[Student]:
        return self.repository.list()