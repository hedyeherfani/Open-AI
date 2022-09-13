from flask import Flask, render_template, request
import config
import os
import sys
sys.path.append("/Users/hedyeherfani/github/Open-AI")
import content


def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())



@app.route('/material-suggestions', methods=["GET", "POST"])
def MaterialSuggestions():

    if request.method == 'POST':
        submission = request.form['materialSuggestions']
        query = "Generate and hook suggestions for crocheting {}".format(submission)
        openAIAnswer = content.openAI(query)
        prompt = 'Your AI suggestion for yarn/hook {} are:'.format(submission)

    return render_template('material-suggestions.html', **locals())



@app.route('/project-suggestions', methods=["GET", "POST"])
def ProjectSuggestions():

    if request.method == 'POST':
        submission = request.form['projectSuggestions']
        query = "Generate 3 suggestions for a crochet project for  {}".format(submission)
        openAIAnswer = content.openAI(query)
        prompt = 'Your 3 AI suggestions for potential crochet projects for {} are:'.format(submission)

    return render_template('project-suggestions.html', **locals())



@app.route('/pattern-creator', methods=["GET", "POST"])
def patternCreator():

    if request.method == 'POST':
        submission = request.form['patternCreator']
        query = "Generate a crochet pattern to make  {}".format(submission)
        openAIAnswer = content.openAI(query)
        prompt = 'Your pattern suggestion to make {} is:'.format(submission)

    return render_template('pattern-creator.html', **locals())



@app.route('/price-suggestion', methods=["GET", "POST"])
def priceSuggestion():

    if request.method == 'POST':
        submission = request.form['priceSuggestion']
        query = "Generate a price suggestion in USD for a crocheted  {}".format(submission)
        openAIAnswer = content.openAI(query)
        prompt = 'Your price suggestion in USD {} is:'.format(submission)

    return render_template('price-suggestion.html', **locals())





if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
