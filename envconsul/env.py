import web
import os
import pprint

urls = ("/.*", "environ")
app = web.application(urls, globals())
pp = pprint.PrettyPrinter(indent=4)

class environ:
    def GET(self):
        return pp.pformat(dict(os.environ))

    if __name__ == "__main__":
        print("starting...")
        app.run()
