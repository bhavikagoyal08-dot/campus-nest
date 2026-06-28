from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import Text

from app.database import Base


class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)

    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    title = Column(String(255), nullable=False)

    description = Column(Text)

    rent = Column(Float)

    address = Column(String(255))

    wifi = Column(Boolean, default=False)

    food = Column(Boolean, default=False)

    ac = Column(Boolean, default=False)

    laundry = Column(Boolean, default=False)

    image_url = Column(String(500), nullable=True)

    latitude = Column(Float, nullable=True)

    longitude = Column(Float, nullable=True)
