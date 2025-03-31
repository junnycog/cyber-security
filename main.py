class User(Base, TimestampMixin):
    # 기존 필드에 추가
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    account_type: Mapped[str] = mapped_column(String(20))  # admin, user 등
    last_login: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
