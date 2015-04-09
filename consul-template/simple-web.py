import web
import os
import sys

urls = ("/.*", "environ")
app = web.application(urls, globals())

class environ:
    def GET(self):
        return "hello from port: " + sys.argv[1] + "\n"

    if __name__ == "__main__":
        app.run()
