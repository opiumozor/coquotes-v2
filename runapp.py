from coquotes import app

if (app.config['DEV_SERVER']):
    app.secret_key = app.config['SECRET']
    app.run(debug=app.config['DEBUG'],
            host=app.config['HOST'],
            port=app.config['PORT'])
