
from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()

    def add_course(self, courses):
        query = "INSERT INTO courses (course_name, description, created_at) VALUES(:course_name, :course_description, NOW())"
        data = {
            'course_name':courses['course_name'],
            'course_description':courses['course_description']
        }
        return self.db.query_db(query,data)

    def show_courses(self):
        query = "SELECT * FROM courses"
        return self.db.query_db(query)

    def show_course_by_id(self, course_id):
        query = "SELECT * FROM courses WHERE id=:course_id"
        data = {
            'course_id':course_id
        }
        return self.db.query_db(query, data)

    def destroy_page(self, course_id):
        query = "SELECT * FROM courses WHERE id=:course_id"
        data = {
            'course_id': course_id
        }
        return self.db.query_db(query, data)

    def confirm(self, course_id):
        query = "DELETE FROM courses WHERE id= :course_id"
        data = {
            'course_id': course_id
        }
        return self.db.query_db(query, data)
