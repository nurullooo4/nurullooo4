from collections import namedtuple
from typing import Optional
from uuid import UUID, uuid4
#
# # ---namedtuple---
#
# Todo = namedtuple('Todo', ['id', 'title', 'description', 'priority'])
#
# mission = Todo(id=uuid4(), title='Test mission', description='Test mission', priority=3)
#
# print(mission)
#
#
# # ---class---
#
# class Todo :
#     def __init__(self, id:Optional[UUID], title:str, description:str, priority:int, created_at:datetime):
#         self.id = id
#         self.title = title
#         self.description = description
#         self.priority = priority
#         self.created_at = created_at
#
#
#
# mission = Todo(id=uuid4(), title='Mission 1', description='Mission 1', priority=1, created_at=self.created_at)
# print(mission)


# def create_account(initial_balance):



