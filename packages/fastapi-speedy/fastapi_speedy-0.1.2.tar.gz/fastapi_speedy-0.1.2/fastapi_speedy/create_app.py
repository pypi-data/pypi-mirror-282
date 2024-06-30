import os
import shutil
import click


@click.command()
@click.argument('app_name')
def create_app(app_name):
    src_dir = os.path.join(os.path.dirname(__file__), 'fastapi_boilerplate')
    dest_dir = os.path.join(os.getcwd(), app_name)

    if os.path.exists(dest_dir):
        print(f"Directory {app_name} already exists")
        return

    shutil.copytree(src_dir, dest_dir)

    # Update pyproject.toml with the new app name
    pyproject_path = os.path.join(dest_dir, 'pyproject.toml')
    if os.path.exists(pyproject_path):
        with open(pyproject_path, 'r') as file:
            pyproject_content = file.read()

        pyproject_content = pyproject_content.replace('fastapi_boilerplate', app_name)

        with open(pyproject_path, 'w') as file:
            file.write(pyproject_content)

    print(f"New FastAPI app created at {dest_dir}")


if __name__ == "__main__":
    create_app()
