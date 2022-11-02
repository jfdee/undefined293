try:
    from .local import LocalSettings as Settings
except ImportError:
    from .main import MainSettings as Settings

settings = Settings()


__all__ = ('settings', )
