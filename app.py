from Flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Set the beta access code
BETA_ACCESS_CODE = "beta1"

@app.route('/')
def home():
    # Render the HTML form from the HTML code above
    return render_template_string(open('index.html').read())

@app.route('/beta', methods=['POST'])
def beta_access():
    access_code = request.form.get('access_code')
    if access_code == BETA_ACCESS_CODE:
        # Display a welcome message or beta content
        return "<h2>Welcome, Beta Member! You have access to exclusive content.</h2>"
    else:
        # Redirect back to home with an error message if code is incorrect
        return "<h2>Access Denied. Incorrect Access Code.</h2><br><a href='/'>Go back</a>"

if __name__ == "__main__":
    app.run(debug=True)
