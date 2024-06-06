from flask import jsonify, abort, make_response
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from app.main.models import Task, User
from app.database import db


class TaskService:
    def list_all_tasks(user_id):
        tasks = Task.query.filter_by(user_id=user_id).all()
        response = [task.serialize()for task in tasks]
        return jsonify(response)

    def create_task(data, user_id):
        try:
            new_task = Task(
                title=data['title'], 
                description=data['description'],
                user_id=user_id
                )
            db.session.add(new_task)
            db.session.commit()
            return make_response(jsonify(new_task.serialize()), 201)

        except Exception as e:
            db.session.rollback()
            abort(400, description=str(e))

    def retrieve_task(task_id, user_id):
        task = Task.query.get_or_404(task_id)
        return jsonify(task.serialize())


    def update_task(task_id, data, user_id):
        task = Task.query.get_or_404(task_id)
        try:
            task.title = data.get('title', task.title)
            task.description = data.get('description', task.description)
            db.session.commit()
            response = Task.query.get(task_id).serialize()
            return jsonify(response)
        except Exception as e:
            db.session.rollback()
            abort(400, description=str(e))

    def delete_task(id, user_id):
        task = Task.query.get_or_404(id)
        try:
            db.session.delete(task)
            db.session.commit()
            return jsonify({"message": "Tarea eliminada!"})
        except Exception as e:
            db.session.rollback()
            abort(400, description=str(e))

class UserService:

    def register(data):
        username = data['username']
        password = data['password']

        if not username or not password:
            return jsonify({'error': 'Se requieren todos los campos'}), 400

        user = User.query.filter_by(username=username).first()
        if user:
            return jsonify({'error': 'El usuario ya existe'}), 400

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

    def login(data):
        username = data['username']
        password = data['password']

        if not username or not password:
            return jsonify({'error': 'Se requieren todos los campos'}), 400

        user = User.query.filter_by(username=username).first()
        if not user or not user.verify_password(password):
            return jsonify({'error': 'Credenciales incorrectas'}), 401

        access_token = create_access_token(identity=user.id)
        return jsonify({'access_token': access_token})
