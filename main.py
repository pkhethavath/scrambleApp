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
import webapp2
import os
import jinja2
import random
import array
current_directory=jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

def selectWord():
    library = ["HOUSE",
             "MOUNTAIN",
             "JOUST",
             "CATTLE",
             "YOUNG",
             "ROUTE",
             "COMPUTER",
             "ACTION",
             "CARD"]
    n=len(library)
    k = random.randint(0,n-1)
    return library[k]

def permute(s1):
    n=len(s1)
    loc=[0]
    for i in range(1,n):
      loc.append(i)
    t=""
    for i in range(0,n):
      k = random.randint(i,n-1)
      t=t+s1[loc[k]]
      loc[k]= loc[i]
    print len(t)
    return t


class MainHandler(webapp2.RequestHandler):
    orig_word=""
    def get(self):
        prog_template = current_directory.get_template("templates/index.html")
        orig_word = selectWord()
        new_word = permute(orig_word)
        self.response.write(prog_template.render({"new_word":new_word,"orig_word":orig_word}))
    def post(self):
        prog_template=current_directory.get_template("templates/index.html")
        guess_word = self.request.get("answer")
        orig_word=self.request.get("clue")
        self.response.write(prog_template.render({"new_word":guess_word}))
        if guess_word == orig_word:
            self.response.write("<br><br><h2>You Got it!</h2>")
        else:
            self.response.write("<br><br><h2>SORRY!</h2>")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
    ], debug=True)
