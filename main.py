from flask import Flask

app = Flask(__name__)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

@app.route('/test')
def test():
    return 'test'

