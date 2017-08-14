#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2, cgi, jinja2, os, re
from google.appengine.ext import db
from datetime import datetime

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

class Quiz (db.Model):
    title = db.StringProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    attempts = db.IntegerProperty (required = True)
    totalscore = db.IntegerProperty (required = True)
    question1 = db.StringProperty(required = True)
    answera1 = db.StringProperty (required = True)
    answerb1 = db.StringProperty (required = True)
    answerc1 = db.StringProperty (required = True)
    answerd1 = db.StringProperty (required = True)
    correct1 = db.StringProperty (required = True)
    question2 = db.StringProperty(required = True)
    answera2 = db.StringProperty (required = True)
    answerb2 = db.StringProperty (required = True)
    answerc2 = db.StringProperty (required = True)
    answerd2 = db.StringProperty (required = True)
    correct2 = db.StringProperty (required = True)
    question3 = db.StringProperty(required = True)
    answera3 = db.StringProperty (required = True)
    answerb3 = db.StringProperty (required = True)
    answerc3 = db.StringProperty (required = True)
    answerd3 = db.StringProperty (required = True)
    correct3 = db.StringProperty (required = True)
    question4 = db.StringProperty(required = True)
    answera4 = db.StringProperty (required = True)
    answerb4 = db.StringProperty (required = True)
    answerc4 = db.StringProperty (required = True)
    answerd4 = db.StringProperty (required = True)
    correct4 = db.StringProperty (required = True)
    question5 = db.StringProperty(required = True)
    answera5 = db.StringProperty (required = True)
    answerb5 = db.StringProperty (required = True)
    answerc5 = db.StringProperty (required = True)
    answerd5 = db.StringProperty (required = True)
    correct5 = db.StringProperty (required = True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        t = jinja_env.get_template("main.html")
        response = t.render()
        self.response.write(response)

class CreateHandler (webapp2.RequestHandler):
    def get(self):
        t = jinja_env.get_template ("create.html")
        response = t.render()
        self.response.write(response)

    def post(self):
        new_title = self.request.get("title")
        new_question1 = self.request.get("question1")
        new_answera1 = self.request.get("answera1")
        new_answerb1 = self.request.get("answerb1")
        new_answerc1 = self.request.get("answerc1")
        new_answerd1 = self.request.get("answerd1")
        new_correct1 = self.request.get("correct1")

        new_question2 = self.request.get("question2")
        new_answera2 = self.request.get("answera2")
        new_answerb2 = self.request.get("answerb2")
        new_answerc2 = self.request.get("answerc2")
        new_answerd2 = self.request.get("answerd2")
        new_correct2 = self.request.get("correct2")

        new_question3 = self.request.get("question3")
        new_answera3 = self.request.get("answera3")
        new_answerb3 = self.request.get("answerb3")
        new_answerc3 = self.request.get("answerc3")
        new_answerd3 = self.request.get("answerd3")
        new_correct3 = self.request.get("correct3")

        new_question4 = self.request.get("question4")
        new_answera4 = self.request.get("answera4")
        new_answerb4 = self.request.get("answerb4")
        new_answerc4 = self.request.get("answerc4")
        new_answerd4 = self.request.get("answerd4")
        new_correct4 = self.request.get("correct4")

        new_question5 = self.request.get("question5")
        new_answera5 = self.request.get("answera5")
        new_answerb5 = self.request.get("answerb5")
        new_answerc5 = self.request.get("answerc5")
        new_answerd5 = self.request.get("answerd5")
        new_correct5 = self.request.get("correct5")

        quiz = Quiz(title = new_title, attempts = 0, totalscore = 0,
        question1 = new_question1, answera1 = new_answera1, answerb1 = new_answerb1, answerc1 = new_answerc1, answerd1 = new_answerd1, correct1 = new_correct1,
        question2 = new_question2, answera2 = new_answera2, answerb2 = new_answerb2, answerc2 = new_answerc2, answerd2 = new_answerd2, correct2 = new_correct2,
        question3 = new_question3, answera3 = new_answera3, answerb3 = new_answerb3, answerc3 = new_answerc3, answerd3 = new_answerd3, correct3 = new_correct3,
        question4 = new_question4, answera4 = new_answera4, answerb4 = new_answerb4, answerc4 = new_answerc4, answerd4 = new_answerd4, correct4 = new_correct4,
        question5 = new_question5, answera5 = new_answera5, answerb5 = new_answerb5, answerc5 = new_answerc5, answerd5 = new_answerd5, correct5 = new_correct5)
        quiz.put()

        t = jinja_env.get_template ("create-confirm.html")
        response = t.render(quiz = quiz)
        self.response.write(response)

class SelectHandler (webapp2.RequestHandler):
    def get(self):
        # Add in a mechanism for creating a list of quizzes, and pass that into the selectquiz template
        t = jinja_env.get_template ("selectquiz.html")
        response = t.render()
        self.response.write(response)

    def post(self):
        # Determine whether or not the TakeHandler is even necessary, or can it be run from here
        #
        # quiz = self.request.get("quiz")

class TakeHandler (webapp2.RequestHandler):
    def get(self):
        t = jinja_env.get_template ("takequiz.html")
        response = t.render()
        self.response.write(response)

    def post(self):

        t = jinja_env.get_template ("takequiz.html")
        response = t.render()
        self.response.write(response)

# Add a post request after the quiz selection has been made
# Reference the quizdisplay template



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/createquiz', CreateHandler),
    ('/takequiz', TakeHandler),
    ('/selectquiz', SelectHandler)
], debug=True)
