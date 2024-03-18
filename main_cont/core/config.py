import logging

from pydantic_settings import BaseSettings, SettingsConfigDict

from core.logging_setup import setup_root_logger

log_levels = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR
}


class Settings(BaseSettings):
    logging_level: str = ...
    project_name: str = 'app'

    model_config = SettingsConfigDict(env_file=".env", extra='allow')

    main_host: str = ...
    main_port: int = ...

    elastic_host: str = ...
    elastic_port: int = ...

    def get_logging_level(self) -> int:
        return log_levels.get(self.logging_level, logging.INFO)


settings = Settings()

setup_root_logger()

# logging.basicConfig(
#     level=settings.get_logging_level(),
#     format='%(levelname)s - %(message)s',
# )
#
logger = logging.getLogger(__name__)


class ElasticDsn(BaseSettings):
    scheme: str = 'http'
    host: str = settings.elastic_host
    port: int = settings.elastic_port


class ElasticSettings(BaseSettings):
    hosts: list[ElasticDsn] = [ElasticDsn()]
    timeout: int = 60
    max_retries: int = 10
    retry_on_timeout: bool = True
