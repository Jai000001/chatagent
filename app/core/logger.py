import logging
import inspect

class Logger:
    """Singleton logger factory with auto-handling"""
    _loggers = {}

    @classmethod
    def get_logger(cls, name: str = None):
        name = name or "root"
        if name not in cls._loggers:
            logger = logging.getLogger(name)

            if not logger.hasHandlers():
                logging.basicConfig(
                    level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                )
                if name == "root":
                    logging.getLogger("httpx").setLevel(logging.WARNING)
                    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
                    logging.getLogger("uvicorn.error").setLevel(logging.INFO)

            cls._loggers[name] = logger
        return cls._loggers[name]
