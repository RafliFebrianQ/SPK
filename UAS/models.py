from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Salmon(Base):
    __tablename__ = 'salmon'
    id_salmon: Mapped[str] = mapped_column(primary_key=True)
    harga: Mapped[int] = mapped_column()
    umur: Mapped[int] = mapped_column()
    berat: Mapped[int] = mapped_column()
    lemak: Mapped[int] = mapped_column()
    omega_3: Mapped[int] = mapped_column()
    
    def __repr__(self) -> str:
        return f"Salmon(id_Salmon={self.id_Salmon!r}, harga={self.harga!r})"
