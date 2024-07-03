from sqlalchemy import Column, String
from zaim_sqlite.model import BaseModel


class Mode(BaseModel):
    """
    種別モデル
    """

    __tablename__ = "modes"
    __table_args__ = {"comment": "種別のマスターテーブル"}

    name = Column(String(255), nullable=False)
