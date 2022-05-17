from flask import Flask,request,render_template
import requests

app = Flask(__name__)



@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        username = request.form.get("githubname")
        api = "https://api.github.com/users/" + username
        response = requests.get(api).json() 
        data = dict()
        data["avatar_url"] = response["avatar_url"]
        data["public_repos"] = response["public_repos"]
        data["public_gists"] = response["public_gists"]
        data["followers"] = response["followers"]
        data["following"] = response["following"]
        data["company"] = response["company"]
        data["blog"] = response["blog"]
        data["location"] = response["location"]
        data["created_at"] = response["created_at"]
        data["html_url"] = response["html_url"]
        # last repositories
        repos = requests.get(api + "/repos").json()
        
        return render_template("index.html",data = data,repos = repos)
    else:
        return render_template("index.html",data = dict(),repos = dict())


if __name__ == "__main__":
    app.run(debug=True)