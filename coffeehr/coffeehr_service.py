from typing import Optional, Any
from datetime import datetime, date

from compose import compose
import pytz

from db import bigquery
from coffeehr.pipeline.interface import Pipeline, Data
from coffeehr.pipeline import pipelines
from coffeehr.coffeehr_repo import get
from tasks import cloud_tasks


TZ = pytz.timezone("Asia/Ho_Chi_Minh")


def _transform_timestamp(schema: list[dict[str, Any]]):
    def _parse_ts(value: Optional[str]) -> Optional[str]:
        return (
            datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
            .replace(tzinfo=TZ)
            .isoformat(timespec="seconds")
            if value
            else None
        )

    def _svc(rows: Data) -> Data:
        return [
            {
                **row,
                **{
                    k: _parse_ts(v)
                    for k, v in row.items()
                    if k in [i["name"] for i in schema if i["type"] == "TIMESTAMP"]
                },
            }
            for row in rows
        ]

    return _svc


def pipeline_service(pipeline: Pipeline) -> int:
    start = date(2017, 1, 1)
    end = date(date.today().year + 1, 1, 1)
    return compose(
        bigquery.load(pipeline.name, pipeline.schema),
        _transform_timestamp(pipeline.schema),
        pipeline.transform,
        get(pipeline.get_options),
    )((start, end))



def create_tasks_service() -> dict[str, int]:
    return {
        "tasks": cloud_tasks.create_tasks(
            "coffeehr",
            [{"table": table} for table in pipelines.keys()],
            lambda x: x["table"],
        )
    }
