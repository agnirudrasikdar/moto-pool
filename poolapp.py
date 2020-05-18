from flask import Flask, render_template
app = Flask(__name__)


posts = [
    {
    'author':'Corey',
    'title': 'Blog Post 1',
    'content': 'First Post content',
    'date_posted': 'April 20, 2018'
    },
{
    'author':'Agni',
    'title': 'Blog Post 2',
    'content': 'Second Post content',
    'date_posted' : 'April 21, 2018'
    }

]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)


@app.route("/driver")
def find_driver():
    return render_template('findDriver.html')

@app.route("/drivermatches")
def finddrivermatches():
    return render_template('findDriverMatches.html')


@app.route("/rider")
def offer_ride():
    return render_template('offerRide.html')

@app.route("/riderrmatches")
def findridermatches():
    return render_template('offerRideMatches.html')


if __name__ == '__main__':
    app.run(debug=True)

