from projen.python import PythonProject

project = PythonProject(
    author_email="flaviostutz@gmail.com",
    author_name="Flavio Stutz",
    module_name="projen_world",
    name="projen_world",
    version="0.1.0",
    deps=["ruff"],
    dev_deps=["poetry"],
    github=False,
)

project.synth()
