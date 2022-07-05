import pytest

from coffeehr.pipeline import pipelines
from coffeehr import coffeehr_service


class TestCoffeeHR:
    @pytest.fixture(
        params=pipelines.values(),
        ids=pipelines.keys(),
    )
    def pipeline(self, request):
        return request.param

    def test_service(self, pipeline):
        res = coffeehr_service.pipeline_service(pipeline)
        assert res >= 0


class TestTasks:
    def test_service(self):
        res = coffeehr_service.create_tasks_service()
        assert res["tasks"] > 0
