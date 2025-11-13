from client.api_client import APIClient
from typing import TypedDict
from httpx import Response

class GetRequestQueryDict(TypedDict):
    
    userId: str

class CreateBodyRequestDict(TypedDict):

    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str

class UpdateBodyRequestDict(TypedDict):

    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None
 

class CoursesClient(APIClient):

    def get_api_courses(self, query:GetRequestQueryDict) -> Response:
        return self.get("/api/v1/courses", params=query)
    
    def get_api_course(self, course_id: str) -> Response:
        return self.get(f"/api/v1/courses{course_id}")
    
    def create_course_api(self, request: CreateBodyRequestDict) -> Response:
        return self.post("/api/v1/courses", json=request)
    
    def update_course_api(self, request: UpdateBodyRequestDict, course_id: str) -> Response:
        return self.patch(f"/api/v1/courses{course_id}", json=request)
    
    def delete_api_course(self, course_id : str) -> Response:
        return self.delete(f"/api/v1/courses{course_id }")