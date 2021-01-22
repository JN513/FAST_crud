# project/app/api/crud.py

from typing import Union
from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary
from fastapi import HTTPException


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )
    await summary.save()
    return summary.id


async def get(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first().values()
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")

    return summary
