from pydantic import BaseModel, ConfigDict


class InboxesType(BaseModel):
    model_config = ConfigDict(frozen=True, extra="ignore")
