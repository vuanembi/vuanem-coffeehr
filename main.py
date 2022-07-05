from typing import Any

from coffeehr import coffeehr_service
from coffeehr.pipeline import pipelines


def main(request):
    data: dict[str, Any] = request.get_json()
    print(data)

    if "tasks" in data:
        response = coffeehr_service.create_tasks_service()
    elif "table" in data:
        response = coffeehr_service.pipeline_service(pipelines[data["table"]])
    else:
        raise ValueError(data)

    print(response)
    return response
