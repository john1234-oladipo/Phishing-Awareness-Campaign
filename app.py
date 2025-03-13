from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Phishing simulation page
@app.route('/simulation')
def simulation():
    return render_template('simulation.html')

# Feedback page
@app.route('/feedback')
def feedback():
    action = request.args.get('action', 'ignored')  # Default to 'ignored' if no action is provided
    return render_template('feedback.html', action=action)

if __name__ == '__main__':
    app.run(debug=True)
