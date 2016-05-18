
from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')
        self.db = self._app.db

    def index(self):
        courses = self.models['Course'].show_courses()
        return self.load_view('index.html', courses = courses)

    def add(self):
        course_details = {
            'course_name':request.form['course_name'],
            'course_description':request.form['description']
        }
        self.models['Course'].add_course(course_details)
        return redirect ('/')

    def destroy_course(self, id):
        courses = self.models['Course'].show_course_by_id(id)
        return self.load_view('destroy.html', courses=courses[0])

    def confirm_destroy(self, id):
        if request.method == 'POST' and request.form['action'] == 'no':
            return redirect ('/')
        else:
            course = self.models['Course'].confirm(id)
            return redirect ('/')
