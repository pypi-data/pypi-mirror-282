import pytest
from unittest.mock import asyncmock, magicmock
from ..controller.controller import controller
from ..model.model import model
from ..view.view import view

@pytest.fixture
def mock_model(mocker):
    mocker.patch('model.model._execute', new=asyncmock(return_value=("mock_output", "")))
    mocker.patch('model.model._get_openai_answer', new=asyncmock(return_value="mock_commit_message"))
    return model(context_path=none, convention_path=none)

@pytest.fixture
def mock_view(mocker):
    return mocker.create_autospec(view, instance=true)

@pytest.fixture
def controller(mock_model, mock_view):
    ctrl = controller({'context_path': none, 'convention_path': none})
    ctrl.model = mock_model
    ctrl.view = mock_view
    return ctrl

def test_generate_commit_no_changes(controller, mock_model):
    mock_model.get_changes_no_split = magicmock(return_value="")
    mock_model.get_files_content = magicmock(return_value=[])
    
    response = controller.model.generate_commit(stages=false, temperature=0.8)
    assert response == "no changes found"

def test_generate_commit_with_changes(controller, mock_model):
    mock_model.get_changes_no_split = magicmock(return_value="mock_diff_output")
    mock_model.get_files_content = magicmock(return_value=[("file1.py", "print('hello, world!')")])
    
    response = controller.model.generate_commit(stages=false, temperature=0.8)
    assert response == "mock_commit_message"

def test_generate_commit_increase_temperature(controller, mock_model):
    mock_model.get_changes_no_split = magicmock(return_value="mock_diff_output")
    mock_model.get_files_content = magicmock(return_value=[("file1.py", "print('hello, world!')")])
    
    controller.model.generate_commit = magicmock(side_effect=["commit_message_1", "commit_message_2"])
    user_input = "r"

    controller.view.display_generated_commit = magicmock(side_effect=[user_input, "a"])
    
    controller.generate_commit()
    
    assert controller.model.generate_commit.call_count == 2

def test_generate_commit_commit_message(controller, mock_model):
    mock_model.get_changes_no_split = magicmock(return_value="mock_diff_output")
    mock_model.get_files_content = magicmock(return_value=[("file1.py", "print('hello, world!')")])
    
    controller.model.generate_commit = magicmock(return_value="commit_message")
    controller.model.commit = asyncmock()

    controller.view.display_generated_commit = magicmock(return_value="c")
    
    controller.generate_commit()

    controller.model.commit.assert_called_once_with("commit_message")

def test_generate_commit_abort(controller, mock_model):
    mock_model.get_changes_no_split = magicmock(return_value="mock_diff_output")
    mock_model.get_files_content = magicmock(return_value=[("file1.py", "print('hello, world!')")])
    
    controller.model.generate_commit = magicmock(return_value="commit_message")
    controller.model.commit = asyncmock()

    controller.view.display_generated_commit = magicmock(return_value="a")
    
    controller.generate_commit()

    controller.model.commit.assert_not_called()