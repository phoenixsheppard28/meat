from sqlmodel import Field, create_engine, SQLModel, Relationship


class BrandCertificationLink(SQLModel, table=True):
    brand_id: str = Field(default=None, foreign_key="brand.id", primary_key=True)
    certification_id: str = Field(
        default=None, foreign_key="certification.id", primary_key=True
    )


class Brand(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    certifications: list["Certification"] = Relationship(
        back_populates="brands", link_model=BrandCertificationLink
    )


class Certification(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    brands: list["Brand"] = Relationship(
        back_populates="certifications", link_model=BrandCertificationLink
    )
