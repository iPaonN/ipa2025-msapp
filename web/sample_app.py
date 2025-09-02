# Add to this file for the sample app lab
from flask import Flask, app
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

from pymongo import MongoClient
from bson import ObjectId

import os

sample = Flask(__name__)

mongo_url = os.environ.get("MONGO_URI")
db_name = os.environ.get("DB_NAME")

data = []

client = MongoClient(mongo_url)
mydb = client[db_name]
mycollection = mydb["myrouter"]


@sample.route("/")
def main():
    data = list(mycollection.find())
    return render_template("index.html", data=data)


@sample.route("/add", methods=["POST"])
def add_router():
    yourname = request.form.get("yourname")
    password = request.form.get("password")
    yourip = request.form.get("yourip")

    if yourname and password and yourip:
        data.append({"yourip": yourip, "yourname": yourname, "password": password})
        mycollection.insert_one(
            {"yourip": yourip, "yourname": yourname, "password": password}
        )
    return redirect("/")


@sample.route("/delete/<idx>", methods=["POST"])
def delete_router(idx):
    try:
        mycollection.delete_one({"_id": ObjectId(idx)})
    except Exception:
        pass
    return redirect(url_for("main"))


interface_status = mydb["interface_status"]


@sample.route("/router/<ip>", methods=["GET"])
def router_detail(ip):
    docs = mydb.interface_status.find({"router_ip": ip}).sort("timestamp", -1).limit(3)
    return render_template("router_detail.html", router_ip=ip, interface_data=docs)


if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080)
