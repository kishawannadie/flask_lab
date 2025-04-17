from flask import render_template
from flask import request

class FlaskInputOutput:

    def Input(self, field, title=None, default=None):
        return request.form.get(field, default)

    def Output(self, student):
        return render_template('form.tpl', it=student, about=render_template('item.tpl', it=student))