from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from helpers import nLoginTrialsInLastHourForEmail,ipAddressesForEmail

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id, owner_email=current_user.email)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/public-notes')
def public_notes():
    notes = Note.query.filter_by(isPublic=True)
    return render_template("public_notes.html", notes=notes, user=None)

@views.route('/make-public', methods=['POST'])
@login_required
def make_public():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            note.isPublic = True
            db.session.commit()
    return jsonify({})

@views.route('/ip-control')
def ip_control():
    global nLoginTrialsInLastHourForEmail,ipAddressesForEmail
    return render_template("ip_control.html", ips=list(ipAddressesForEmail[str(current_user.email)]), user=current_user)