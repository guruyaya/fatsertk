from pydantic import BaseModel, Field

class FastModel(BaseModel):
    pass


def FastField(*args, **kwargs):
    Field(*args, **kwargs)

