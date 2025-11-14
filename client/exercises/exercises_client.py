from httpx import Response
from client.api_client import APIClient
from typing import TypedDict


class GetRequestQueryDict(TypedDict):
    courseId: str

class CreateRequestBodyDict(TypedDict):
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int | None
    description: str
    estimatedTime: str

class UpdateRequestBodyDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):

    def get_exercises_api(self, query: GetRequestQueryDict) -> Response:
        return self.get("/api/v1/exercise", params=query)
    
    def get_exercise_api(self, exercise_id: str) -> Response:
        return self.get(f"/api/v1/exercise{exercise_id}")
    
    def create_exercise_api(self, request: CreateRequestBodyDict ) -> Response:
        return self.post("/api/v1/exercise", json=request)
    
    def update_exercise_api(self, request: UpdateRequestBodyDict, exercise_id: str) -> Response:
        return self.patch(f"/api/v1/exercise{exercise_id}", json=request)
    
    def delete_exercise_api(self, exercise_id: str) -> Response:
        return self.delete(f"/api/v1/exercise{exercise_id}")