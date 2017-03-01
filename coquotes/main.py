import json
from coquotes import app
from flask import render_template, make_response, request, redirect, url_for
from coquotes.auth import requires_auth


@app.route("/")
def index():
    """
    """
    try:
        f = open(app.config["QUOTES_FILE"], "r").read()
    except IOError:
        return make_response("Can't open quote file", 500)
    quotes_list = json.loads(f)
    return render_template("quotes.html", quotes=quotes_list)


@app.route("/admin")
@requires_auth
def add_quote_form():
    """
    """
    return render_template("add_quote.html")


@app.route("/add_process", methods=['POST'])
@requires_auth
def add_quote():
    """
    """
    name = request.form['name']
    quote = request.form['quote']
    if len(name) < 2 or len(quote) < 2:
        return make_response("Oops something went wrong!")

    try:
        quote_list = open(app.config["QUOTES_FILE"]).read()
    except IOError:
        quote_list = '[]'
    entries = json.loads(quote_list)
    new_quote = {'name': name, 'quote': quote}
    entries.insert(0, new_quote)
    try:
        open(app.config["QUOTES_FILE"], 'w').write(json.dumps(entries, indent=2, sort_keys=True))
    except IOError:
        return make_response("Can't add quote", 500)

    return redirect(url_for('index'))
