#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 09:19:59 2018

@author: ayoub
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 17:05:29 2018
@author: Ayoub
"""
import flask



app = flask.Flask(__name__)


def HTMLForm():
    form = """<!-- CSS Styles -->
<style>
  .speech {border: 1px solid #DDD; width: 300px; padding: 0; margin: 0}
  .speech input {border: 0; width: 240px; display: inline-block; height: 30px;}
  .speech img {float: right; width: 40px }
</style>

<!-- Search Form -->
<form id="labnol" action="text2onto" method = "post">
  <div class="speech">
    <input type="text" name="q" id="transcript" placeholder="Speak" />

    <img onclick="startDictation()" src="//i.imgur.com/cHidSVu.gif" />
    

  </div>
  <input type="submit" value="Submit">
  
</form>

<!-- HTML5 Speech Recognition API -->
<script>
  function startDictation() {

    if (window.hasOwnProperty('webkitSpeechRecognition')) {

      var recognition = new webkitSpeechRecognition();

      recognition.continuous = false;
      recognition.interimResults = false;

      recognition.lang = "fr-FR";
      recognition.start();

      recognition.onresult = function(e) {
        document.getElementById('transcript').value
                                 = e.results[0][0].transcript;
      
        recognition.stop();
      
      };

      recognition.onerror = function(e) {
        recognition.stop();
      }

    }
  }
</script> """
    return form






@app.route("/text2onto", methods = ['GET', 'POST'])
def formPage():
    html = "<html> <body>" + HTMLForm()
    if flask.request.method == "POST":
      text_input = flask.request.form["q"]
      html += "<p> This is your input: " + text_input + "</p>"
      text_output ="ok"
      html += "<p> This is your text: " + text_output + "</p>"
    html += "</body> </html>"
    return html

if __name__ == "__main__":
    app.run()