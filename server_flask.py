# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 17:05:29 2018

@author: Ayoub
"""
import flask
import closest_word2vec
import parser
from closest_word2vec import *
from parser import text_parser

app = flask.Flask(__name__)


def HTMLForm():
    form = """<form action="text2onto" method = "post">
  Please enter some text ! <br>
  <input type="text" name="your_text" > <br>

  <input type="submit" value="Submit">
</form> """
    return form

def pre_ontology2ontology(pre_ontology):

    pre_aggregation = pre_ontology[0]
    pre_metric = pre_ontology[1]
    pre_dimensions = pre_ontology[2]
    pre_filters = pre_ontology[3]

    aggregation = closestAggregation(pre_aggregation,1)
    metric = closestMetrics(pre_metric,1)
    dimensions = []
    for pre_dimension in pre_dimensions :
      dimensions.append(closestDimensions(pre_dimension,1))
    filters = []
    for pre_filter in pre_filters :
      filters.append(closestFilters(pre_filter,1))

    return([aggregation,metric,dimensions,filters])




@app.route("/text2onto", methods = ['GET', 'POST'])
def formPage():
    html = "<html> <body>" + HTMLForm()
    if flask.request.method == "POST":
      text_input = flask.request.form["your_text"]
      html += "<p> This is your input: " + text_input + "</p>"
      text_output = str(pre_ontology2ontology(text_parser(text_input)))
      html += "<p> This is your text: " + text_output + "</p>"
    html += "</body> </html>"
    return html

if __name__ == "__main__":
    app.run()

