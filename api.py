import responder

api = responder.API()

@api.route("/")
def hello_world(req, resp):
    resp.text = "Wrong route, Mr. Potter!"

@api.route('/snippet')
def snippets(req, resp):
    resp.text = "I'm a delicious snippet!"

api.run()