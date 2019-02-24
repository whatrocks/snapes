import responder
from managers.scraper import get_text_from_url

# TODO: fix this for production or dev
api = responder.API()

@api.route("/")
def hello_world(req, resp):
    resp.text = "Wrong route, Mr. Potter! 10 points from Gryfinndor!"

@api.route('/snippet')
def snippets(req, resp):
    resp.text = get_text_from_url("https://en.wikipedia.org/wiki/Cheese")

if __name__ == "__main__":
    api.run()