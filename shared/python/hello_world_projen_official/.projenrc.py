from projen.python import PythonProject

project = PythonProject(
    author_email="flaviostutz@gmail.com",
    author_name="Flavio Stutz",
    module_name="hello_world_projen_official",
    name="hello_world_projen_official",
    version="0.1.0",
    deps=["ruff"],
    dev_deps=["poetry"],
    github=False,
    commit_generated=False
)

project.synth()
