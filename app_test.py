from flask import Flask, request, render_template
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route("/home")
def home():
    app.logger.info('Info level log')
    app.logger.warning('Warning level log')
    app.logger.critical('Critical level log')
    app.logger.error('Error level log')
    return 'Welcome to the Application!'  

if __name__ == "__main__":
    app.run(debug=True)
