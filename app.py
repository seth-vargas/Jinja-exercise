from stories import story
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension as debugger

app = Flask(__name__)
app.config['SECRET_KEY'] = "key"

debug = debugger(app)

@app.route('/')
def show_form():
    """Generate and show form"""

    prompts = story.prompts
    return render_template("index.html", prompts=prompts)


@app.route('/story')
def show_story():
    """Show story on screen"""

    text = story.generate(request.args)
    return render_template("story.html", text=text)