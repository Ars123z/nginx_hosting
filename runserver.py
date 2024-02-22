from waitress import serve

from practice.wsgi import application

if __name__== "__main__":
    serve(application, host = "localhost", port="8080")