from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route to display the portfolio page
@app.route('/')
def index():
    return render_template('index.html')


# Route to handle POST requests for skills and feedback forms
@app.route('/', methods=['POST'])
def process_form():
    # Check if the "PROJEYİ GÖSTER" button for Python was clicked
    button_python = request.form.get('button_python')
    if button_python:
        # If the Python button was clicked, render the page with the project visible
        return render_template('index.html', button_python=button_python)

    # Check if the feedback form was submitted by looking for the 'email' field
    email = request.form.get('email')
    text = request.form.get('text')
    
    if email and text:
        # For a real application, you would save this data to a database.
        # For now, we'll just print it to the console to show it's received.
        print(f"Geri bildirim alındı:")
        print(f"E-posta: {email}")
        print(f"Yorum: {text}")
        
        # We redirect to the same page to prevent the form from being submitted again
        # if the user refreshes the page (Post/Redirect/Get pattern).
        return redirect(url_for('index'))
        
    # If a form was submitted but it wasn't one we expected,
    # just redirect back to the index page.
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
