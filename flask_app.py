from flask import Flask
import pkg_resources
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'FLASK VERSION = '+pkg_resources.get_distribution('flask').version

if __name__ == '__main__':
    app.run()