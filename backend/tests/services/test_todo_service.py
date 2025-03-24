import unittest
from unittest.mock import MagicMock, patch
from fastapi import HTTPException, status
from src.services.todo_service import TodoService
from src.repositories import TodoRepository
from src.schemas.request import UpdateTodoRequestSchema
from src.models import Todo

class TestTodoService(unittest.TestCase):

    def setUp(self):
        self.mock_repository = MagicMock(spec=TodoRepository)
        self.todo_service = TodoService(repository=self.mock_repository)

    def test_update_todo_success(self):
        user_id = 1
        todo_id = 1
        todo_data = UpdateTodoRequestSchema(id=todo_id, description="Updated description")
        existing_todo = Todo(id=todo_id, user_id=user_id, description="Old description")

        self.mock_repository.get.return_value = existing_todo
        self.mock_repository.update.return_value = existing_todo

        updated_todo = self.todo_service.update_todo(user_id, todo_data)

        self.mock_repository.get.assert_called_once_with(todo_id)
        self.mock_repository.update.assert_called_once_with(existing_todo)
        self.assertEqual(updated_todo.description, "Updated description")

    def test_update_todo_not_found(self):
        user_id = 1
        todo_id = 1
        todo_data = UpdateTodoRequestSchema(id=todo_id, description="Updated description")

        self.mock_repository.get.return_value = None

        with self.assertRaises(HTTPException) as context:
            self.todo_service.update_todo(user_id, todo_data)

        self.assertEqual(context.exception.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(context.exception.detail, 'To-do not found')
        self.mock_repository.get.assert_called_once_with(todo_id)
        self.mock_repository.update.assert_not_called()

    def test_update_todo_unauthorized(self):
        user_id = 1
        todo_id = 1
        todo_data = UpdateTodoRequestSchema(id=todo_id, description="Updated description")
        existing_todo = Todo(id=todo_id, user_id=2, description="Old description")

        self.mock_repository.get.return_value = existing_todo

        with self.assertRaises(HTTPException) as context:
            self.todo_service.update_todo(user_id, todo_data)

        self.assertEqual(context.exception.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(context.exception.detail, 'To-do doesn\'t belong to user')
        self.mock_repository.get.assert_called_once_with(todo_id)
        self.mock_repository.update.assert_not_called()

if __name__ == '__main__':
    unittest.main()