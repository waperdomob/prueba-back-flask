from flask import Blueprint
from flask_restful import Api
from .views import TasksList, Task

task_routes = Blueprint('task', __name__)
api = Api(task_routes)

api.add_resource(TasksList, '/tasks')
api.add_resource(Task, '/tasks/<int:id>')