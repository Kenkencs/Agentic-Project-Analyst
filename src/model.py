from pydantic import BaseModel


class ProductAnalysis(BaseModel):
    problem: str
    severity: int
    evidence: list[str]
    recommendation: str