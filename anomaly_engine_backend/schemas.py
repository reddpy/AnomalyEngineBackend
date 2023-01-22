import datetime

from pydantic import BaseModel


class DataIngestPost(BaseModel):
    payload: str
    endpoint: str
    method: str | None = None


class DataIngest(BaseModel):
    id: int
    data_def_id: int
    data_ingest: str
    created_time: datetime.datetime
