""" Testbed node-related functionality. """

from flask import Blueprint
from flask import request, render_template, flash, redirect, \
                  url_for

from database import db
from models.node import Node

bpNode = Blueprint("node", __name__, template_folder="../templates")

@bpNode.route("/")
def index():
    return redirect(url_for(".list"))

@bpNode.route("/list")
def list():
    nodes = Node.query.all()
    return render_template("node/list.html", nodes=nodes)

@bpNode.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("node/add.html")
    elif request.method == "POST":
        id = request.form["id"]
        node = Node(id)
        db.session.add(node)
        db.session.commit()
        flash("Node '%d' added successfully" % node.id)
        return redirect(url_for(".show", id=node.id))

@bpNode.route("/remove/<id>")
def remove(id):
    node = Node.query.get_or_404(id)
    db.session.delete(node)
    db.session.commit()
    return redirect(url_for(".list"))

@bpNode.route("/show/<id>")
def show(id):
    node = Node.query.get_or_404(id)
    return render_template("node/show.html", node=node)
