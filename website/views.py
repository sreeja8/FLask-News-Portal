from unicodedata import category
from unittest import result
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user #to access all info about the currently logged in user
from .models import Note, User
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    note1 = Note.query.all()

    return render_template("home.html", result=note1, user=current_user)


@views.route('/editor_news', methods=['GET', 'POST']) #decorator
@login_required
def editor_news():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("editor_news.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_route():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    #return render_template("editor_news.html", user=current_user)       
    return jsonify({})