import os
import sys
import tempfile

from flask_ignite import setup_flask_project


def test_default_project_creation(monkeypatch):
    # Use a temporary directory for testing
    with tempfile.TemporaryDirectory() as tmpdirname:
        monkeypatch.chdir(tmpdirname)
        # Set up sys.argv to simulate calling the CLI without a custom project name
        sys.argv = ["flask-ignite"]

        # Execute the main function to create the project structure
        setup_flask_project.main()

        # Check that the default project directory "flask_app" exists
        project_path = os.path.join(tmpdirname, "flask_app")
        assert os.path.isdir(project_path)

        # Verify key files exist
        for filename in ["run.py", "requirements.txt", "config.py"]:
            file_path = os.path.join(project_path, filename)
            assert os.path.isfile(file_path)


def test_custom_project_creation(monkeypatch):
    custom_project = "my_flask_project"
    with tempfile.TemporaryDirectory() as tmpdirname:
        monkeypatch.chdir(tmpdirname)
        # Set up sys.argv to simulate passing a custom project name argument
        sys.argv = ["flask-ignite", "--project", custom_project]

        # Execute the main function to create the project structure
        setup_flask_project.main()

        # Check that the custom project directory exists
        project_path = os.path.join(tmpdirname, custom_project)
        assert os.path.isdir(project_path)

        # Verify key files exist
        for filename in ["run.py", "requirements.txt", "config.py"]:
            file_path = os.path.join(project_path, filename)
            assert os.path.isfile(file_path)
