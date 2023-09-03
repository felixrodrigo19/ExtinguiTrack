import os.path

from app import create_app

if __name__ == "__main__":
    config_filename = os.path.join(os.path.abspath(os.path.curdir), 'pyproject.toml')
    app = create_app(config_filename=config_filename)

    app.run()
