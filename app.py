from flask import Flask, render_template
app = Flask(__name__)

JOBS = [
    {
        "id" : 1 ,
        "title" : "Data Analyst",
        "location" : "Bengaluru , India",
        "salary" : "Rs. 500000"
    } ,
      {
        "id" : 2 ,
        "title" : "Risk Analyst",
        "location" : "Bengaluru , India",
        "salary" : "Rs. 800000"
    },  {
        "id" : 3 ,
        "title" : "Backend Engg",
        "location" : "Hyderabad , India",
        "salary" : "Rs. 1000000"
    },  {
        "id" : 4 ,
        "title" : "Frontend Engg",
        "location" : "Noida , India",
        "salary" : "Rs. 500000"
    }
]

@app.route("/")
def home():
    return render_template("home.html" ,jobs =JOBS)

if __name__=="__main__":
    app.run(debug=True)

