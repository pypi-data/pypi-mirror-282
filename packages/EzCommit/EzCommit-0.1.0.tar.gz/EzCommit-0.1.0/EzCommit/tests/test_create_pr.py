import pytest
from unittest.mock import magicmock, patch

from ..controller.controller import controller
from ..config import ezcommitconfig
from github import githubexception
from openai import authenticationerror

@pytest.fixture
def mock_config():
    config = magicmock(spec=ezcommitconfig)
    config.repo_path = '/home/hoaithi/angular-project/meogroup-backend'
    config.db_path = '/home/hoaithi/angular-project/meogroup-backend/.ezcommit/db'
    config.convention_path = '/home/hoaithi/angular-project/meogroup-backend/.ezcommit/default_convention.txt'
    return config

@pytest.fixture
def mock_model():
    model = magicmock()
    model.get_current_branch.return_value = 'test'
    model.list_all_branches.return_value = ['main', 'test']
    model.repository.get_repo_name.return_value = 'meogroup-backend'

    return model

@pytest.fixture
def mock_view():
    view = magicmock()
    return view

@pytest.fixture
def controller(mock_model, mock_view, mock_config):
    with patch('controller.controller.model', return_value=mock_model):
        with patch('controller.controller.view', return_value=mock_view):
            with patch('config.ezcommitconfig.load_config', return_value=mock_config):
                return controller(config=mock_config)

@patch('click.prompt')
def test_create_pull_request_success(mock_click_prompt, controller, mock_model, mock_view):
    # arrange
    mock_model.create_pr_content.return_value = ('pr content', 'pr title')
    mock_model.create_pull_request.return_value = magicmock(html_url='http://example.com/pr')
    mock_click_prompt.return_value = 'main'
    
    # act
    controller.create_pull_request()

    # assert
    mock_view.display_notification.assert_called_once()

    # clean
    mock_model.reset_mock()
    mock_view.reset_mock()


@patch('click.prompt')
def test_create_pull_request_exit(mock_click_prompt, controller, mock_model, mock_view):
    # arrange
    mock_view.display_selection.return_value = 'exit'
    
    # act
    controller.create_pull_request()

    # assert
    mock_view.display_notification.assert_not_called()
    mock_view.display_error.assert_not_called()
    mock_model.create_pr_content.assert_not_called()
    mock_model.create_pull_request.assert_not_called()

    # clean
    mock_model.reset_mock()
    mock_view.reset_mock()

@patch('click.prompt')
def test_create_pull_request_invalid_branch(mock_click_prompt, controller, mock_model, mock_view):
    # arrange
    mock_view.display_selection.side_effect = ['invalid_branch', 'exit']
    
    # act
    controller.create_pull_request()

    # assert
    mock_view.display_notification.assert_called_with("invalid branch selected")

    # clean
    mock_model.reset_mock()
    mock_view.reset_mock()

@patch('click.prompt')
def test_create_pull_request_valid_branch_as_digit(mock_click_prompt, controller, mock_model, mock_view):
    # arrange
    mock_view.display_selection.side_effect = ['1', 'exit']
    
    # act
    controller.create_pull_request()

    # assert
    mock_model.create_pr_content.assert_called_once_with('test', 'main')
    mock_view.display_error.assert_called_once()

    # clean
    mock_model.reset_mock()
    mock_view.reset_mock()

@patch('click.prompt')
def test_create_pull_request_github_exception(mock_click_prompt, controller, mock_model, mock_view):
    # arrange
    error = githubexception(404, data={'errors': [{'message': 'github error'}]})
    mock_model.create_pull_request.side_effect = error
    mock_view.display_selection.side_effect = ['main', 'exit']
    mock_model.create_pr_content.return_value = ('pr content', 'pr title')
    
    # act
    controller.create_pull_request()

    # assert
    mock_view.display_error.assert_called_with('github error')

class mockauthenticationerror(exception):
    def __init__(self, message, body=none):
        self.body = body or {'message': message}
        super().__init__(message)

@patch('click.prompt')
def test_create_pull_request_authentication_error(mock_click_prompt, controller, mock_model, mock_view):
    # arrange
    error = mockauthenticationerror("auth error", body={'message': 'auth error'})
    mock_model.create_pr_content.side_effect = error
    mock_view.display_selection.side_effect = ['main', 'exit']
    
    # act
    controller.create_pull_request()

    # assert
    mock_view.display_error.assert_called_with('unknown error')
    
    # clean
    mock_model.reset_mock()
    mock_view.reset_mock()

@patch('click.prompt')
def test_create_pull_request_generic_exception(mock_click_prompt, controller, mock_model, mock_view):
    # arrange
    mock_model.create_pr_content.side_effect = exception("unknown error")
    mock_view.display_selection.side_effect = ['main', 'exit']
    
    # act
    controller.create_pull_request()

    # assert
    mock_view.display_error.assert_called_with('unknown error')
    
    # clean
    mock_model.reset_mock()
    mock_view.reset_mock()


@patch('openai.authenticationerror')
def test_create_pull_request_openai_api_key_error(mock_auth_error, controller, mock_model, mock_view):
    # arrange
    error_instance = mock_auth_error
    mock_model.create_pr_content.side_effect = error_instance

    mock_view.display_selection.side_effect = ['main', 'exit']
    
    # act
    controller.create_pull_request()

    # assert
    mock_view.display_error.assert_called_with('unknown error')
    
    # clean
    mock_model.reset_mock()
    mock_view.reset_mock()
