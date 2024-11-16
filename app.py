from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title="AK Tower")

@app.route('/rentflat')
def rentflat():
    return render_template('rentflat.html', title="Rent Flat - AK Tower")

@app.route('/bookseat')
def bookseat():
    return render_template('bookseat.html', title="Book Library Seat - AK Tower")

@app.route('/contact-booking')
def contact_booking():
    return render_template('contact_booking.html', title="Contact Us For Booking - AK Tower")

if __name__ == '__main__':
    app.run(debug=True)
