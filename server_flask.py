# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 17:05:29 2018

@author: Ayoub
"""
import flask
import closest_word2vec
import parser

app = flask.Flask(__name__)


def HTMLForm():
    form = """<form action="text2onto" method = "post">
  Please enter some text ! <br>
  <input type="text" name="your_text" > <br>

  <input type="submit" value="Submit">
</form> """
    return form

@app.route("/text2onto", methods = ['GET', 'POST'])
def formPage():
    html = "<html> <body>" + HTMLForm()
    if flask.request.method == "POST":
      text_input = flask.request.form["your_text"] 
      html += "<p> This is your text: " + str(parser(text_input))
    html += "</body> </html>"
    return html

if __name__ == "__main__":
    app.run()

