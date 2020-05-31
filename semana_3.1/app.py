import web

urls = ('/(.*)', 'mvc.controllers.cookie.Cookie')

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()