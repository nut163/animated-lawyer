from flask import Flask, render_template, request, flash
from schema import Schema, And, Use

app = Flask(__name__)

# Define the schemas
contactFormSchema = Schema({
    'name': And(str, len),
    'email': And(str, len),
    'message': And(str, len)
})

servicesSchema = Schema({
    'service_name': And(str, len),
    'service_description': And(str, len)
})

# Define the services
services = [
    {'service_name': 'Criminal Law', 'service_description': 'We provide legal assistance in criminal cases.'},
    {'service_name': 'Family Law', 'service_description': 'We provide legal assistance in family disputes.'},
    # Add more services as needed
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html', services=services)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        try:
            contactFormSchema.validate(form_data)
            flash('formSubmissionSuccess')
        except:
            flash('formSubmissionError')
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)