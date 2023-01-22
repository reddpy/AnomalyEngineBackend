from sqlalchemy.orm import Session


from . import models, schemas


def store_ingest(db: Session, DataIngest: schemas.DataIngestPost)->schemas.DataIngest:
    new_ingest = models.DataIngestRecord(
        data_ingest=DataIngest.payload, data_def_id=1)

    db.add(new_ingest)
    db.commit()
    db.refresh(new_ingest)

    return new_ingest
