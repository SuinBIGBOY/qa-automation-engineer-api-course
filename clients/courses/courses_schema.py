from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema

class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id: str
    title: str
    max_score: int
    min_score: int
    description: str
    preview_file: FileSchema
    estimated_time: str
    created_by_user: UserSchema

class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema

class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    user_id: str

class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    title: str
    max_score: int | None
    min_score: int | None
    description: str
    estimated_time: str | None
    preview_file_id: str
    created_by_user_id: str

class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    title: str | None
    max_score: int | None
    min_score: int | None
    description: str | None
    estimated_time: str | None