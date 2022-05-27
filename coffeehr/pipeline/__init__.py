from coffeehr.pipeline import departments, employees

pipelines = {i.name: i for i in [j.pipeline for j in [departments, employees]]}  # type: ignore
