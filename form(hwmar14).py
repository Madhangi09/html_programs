from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def form():
    if request.methods=='POST':
        data={
        "Email":request.form.get("mail"),
        "Number":request.form.get("num"),
        "Gender":request.form.get("gender"),
        "Skills":request.form.get("skills"),
        "Department":request.form.get("dept"),
        "Date of Joining":request.form.get("date"),
        "file":request.files.get("file").filename if request.files.get("file") else "No file uploaded"     
        }
        return render_template("result(hwmar14).html",data=data)
    return render_template("(hw_14_03_25).html")
if __name__=="__main__"
    app.run(debug=True)
    