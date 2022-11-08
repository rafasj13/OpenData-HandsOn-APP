from flask import Flask, render_template, jsonify, request
import glob
import os



saving = 0
count = 1

#glob.glob(your/path) is used to select the files of a certain folder
#I want to delete al the path files every time that the server is
#relaunched

files = glob.glob('static/txt/*')
for f in files:
    os.remove(f)


app = Flask(__name__)

@app.route('/')
def home():
    #count the number of path files
    Npaths=len(glob.glob("static/txt/*"))
    return render_template('gpsTask/Location.html', Npaths = Npaths)




@app.route('/UpdateLocation', methods=['GET', 'POST'])
def UpdateLocation():
    
    #saving is a global variable that is only set up to 1 if we post it on /save route.
    #it is used to indicate whether or not a new file must be created. 
    #count is a variable that is used for changing the name of the coordinates files
    global saving, count
   
   #check if a POST request has been made
    if request.method ==  "POST":
        
        #store the data
        lat = float(request.form['lat'])
        long = float(request.form['long'])

        print(lat, " , ", long)
        
        #creates a dictionary
        coords = {"Lat": lat, "Lng":long}
        print("save: ",saving)

        #checks if another file to record the coordinates must be created
        if saving == 1:

            #if that's the case, count increments by 1 and another empty txt file is created
            count+=1
            with open('static/txt/coords'+str(count)+'.txt','w') as f:
                f.write("")
            
            #saving is set up again to 0
            saving=0
        

        #the coordinates are then saved in the new file
        with open('static/txt/coords'+str(count)+'.txt','a') as f:
            f.write("\n"+str(coords))


        return jsonify(coords)


@app.route('/save', methods=['GET', 'POST'])
def save():
    global saving
    if request.method ==  "POST":
        saving = float(request.form['save'])
        print(saving)
    return jsonify(saving)


@app.route('/LastPath')
def LastPath():
    Npaths=len(glob.glob("static/txt/*"))
    return render_template('gpsTask/LastPath.html',Npaths = Npaths)

@app.route('/style')
def style():
    return render_template('style.html')


@app.route('/txt')
def txt():
    return render_template('txt.html')

@app.route('/TrackingMap')
def TrackingMap():
    return render_template('gpsTask/TrackingMap.html')


app.run()
