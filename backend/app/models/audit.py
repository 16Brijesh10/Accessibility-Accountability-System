from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Date,
    DateTime,
    ForeignKey,
)

from sqlalchemy.sql import func

from app.database import Base


class Audit(Base):
    __tablename__ = "audits"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    building_id = Column(
        Integer,
        ForeignKey("buildings.id"),
        nullable=False,
    )

    # ========================================================
    # ACCESSIBILITY STANDARD USED FOR THIS AUDIT
    # ========================================================

    standard_id = Column(
        Integer,
        ForeignKey("standards.id"),
        nullable=True,
    )

    auditor = Column(
        String(255),
        nullable=False,
    )

    audit_date = Column(
        Date,
        nullable=False,
    )

    description = Column(
        Text,
        nullable=True,
    )

    status = Column(
        String(50),
        nullable=False,
        default="completed",
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )