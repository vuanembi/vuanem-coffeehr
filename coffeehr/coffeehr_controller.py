from typing import Any

from coffeehr.pipeline import pipelines
from coffeehr.coffeehr_service import pipeline_service


def controller(body: dict[str, Any]):
    res = pipeline_service(pipelines[body["table"]])
    return {"results": res}
