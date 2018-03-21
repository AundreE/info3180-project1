"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os, random, datetime, uuid
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort, make_response, jsonify, make_response
from forms import SignUpForm
from models import UserProfile
from werkzeug.utils import secure_filename


###
# Routing for your application.
###

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route('/profile', methods=["GET", "POST"])
def profile():
    form = SignUpForm()
    
    if request.method == "POST":
        file_folder = app.config['UPLOAD_FOLDER']
        
        if form.validate_on_submit():
            
            # get form data
            fname = form.first_name.data
            lname = form.last_name.data
            gender = form.gender.data
            email = form.email.data
            location = form.location.data
            biography = form.biography.data
            created = str(datetime.datetime.now()) 
            
            # get and save the image
            pic = request.files['image']
            image = secure_filename(pic.filename)
            
            #validate file upload on submit
            pic.save(os.path.join(app.config['UPLOAD_FOLDER'], image))
            
            # generate unique user id
            userid = str(uuid.uuid3(uuid.NAMESPACE_DNS, str(fname)))
            
            #Save data to database
            new_user = UserProfile(userid,fname,lname,gender,email,location,biography,image, created_on)
           
                
            db.session.add(new_user)
            db.session.commit()
            
            flash("Created Successfully", "success")
            return redirect(url_for("profile"))
        flash_errors(form)
    print form.errors.tems()    
    return render_template("signup.html", form=form)
   
@app.route('/profiles', methods=["GET", "POST"])
def profiles():
    users = UserProfile.query.all()
    user_list =[{"userid":user.userid,"FirstName": user.fname, "LastName": user.lname, "gender": user.gender, "Location": user.location} for user in users]
    
    if request.method == "GET":
        if users is not None:
            file_folder = app.config['UPLOAD_FOLDER']
            return render_template("view_all.html", user_list=users)
    
    elif request.method == "POST":
        response = make_response(jsonify({"users": user_list}))                                           
        response.headers['Content-Type'] = 'application/json'            
        return response
    
@app.route('/profile/<userid>', methods=["GET", "POST"])
def get_profile(userid):
    
    user = UserProfile.query.filter_by(userid=userid).first()
    if user is not None:
        return render_template('profile.html',user=user)
    else:
        flash('Unable to view user profile', 'danger')
        return redirect(url_for('profile'))




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
