from flask import Flask, render_template, request, redirect
from datetime import datetime 


app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    totalItems= int(request.form['strawberry'])+int(request.form['raspberry'])+int(request.form['apple'])
    current_date_time = datetime.now().strftime("%B %dth %Y %I:%M:%S %p")
    print(f"Charging {request.form['first_name']} for {totalItems} fruits")
    return render_template("checkout.html",users_infos = request.form, total_items = totalItems ,currentDatetime = current_date_time  )

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")


@app.errorhandler(404)  # we specify in parameter here the type of error, here it is 404
def page_not_found(
    error,
):  # (error) is important because it recovers the instance of the error that was thrown
    return f"<h2 style='text-align:center;padding-top:40px'>Sorry! No response. Try again</h2>"


if __name__=="__main__":   
    app.run(debug=True)    