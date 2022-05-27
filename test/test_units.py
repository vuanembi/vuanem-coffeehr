import pytest

from coffeehr.pipeline import pipelines
from coffeehr.coffeehr_service import pipeline_service
from tasks.tasks_service import create_tasks_service


class TestCoffeeHR:
    @pytest.fixture(
        params=pipelines.values(),
        ids=pipelines.keys(),
    )
    def pipeline(self, request):
        return request.param

    def test_service(self, pipeline):
        res = pipeline_service(pipeline)
        assert res >= 0


class TestTasks:
    def test_service(self):
        res = create_tasks_service()
        assert res["tasks"] > 0
