from pydantic import BaseModel

'''
create your schema models here
'''


class DataIngestPost(BaseModel):
    payload: str
    endpoint: str
    method: str | None = None
