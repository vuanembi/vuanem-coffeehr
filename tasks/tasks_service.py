from coffeehr.pipeline import pipelines
from tasks.cloud_tasks import create_tasks


def create_tasks_service() -> dict[str, int]:
    return {
        "tasks": create_tasks(
            "coffeehr",
            [{"table": table} for table in pipelines.keys()],
            lambda x: x["table"],
        )
    }
