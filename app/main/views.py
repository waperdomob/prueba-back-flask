from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from .services import TaskService

class TasksList(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        return TaskService.list_all_tasks(user_id)

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        data = request.get_json()
        return TaskService.create_task(data, user_id)

class Task(Resource):
    @jwt_required()
    def get(self, id):
        user_id = get_jwt_identity()
        task = TaskService.retrieve_task(id, user_id)
        return task

    @jwt_required()
    def put(self, id):
        user_id = get_jwt_identity()
        data = request.get_json()
        return TaskService.update_task(id, data, user_id)

    @jwt_required()
    def delete(self, id):
        user_id = get_jwt_identity()
        return TaskService.delete_task(id, user_id)
    

    