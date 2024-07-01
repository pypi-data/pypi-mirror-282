import json
import os

from config.load_env import load_secrets
from loggers.aws_logger import AWSLogger
from loggers.gcp_logger import GCPLogger
from loggers.local_logger import LocalLogger


class LoggerFactory2:
    def __init__(self, config_file='config.json'):
        self.logger = None
        self.config_file = config_file

    def get_logger(self):
        if self.logger:
            return self.logger

        with open(self.config_file, 'r') as f:
            config = json.load(f)

        environment = config.get('environment')

        print('Environment: ' + environment)

        if environment == 'aws':
            aws_config = config.get('aws', {})
            # Load secrets from AWS Secrets Manager
            load_secrets(aws_config)
            os.environ['RETENTION_DAYS'] = aws_config.get('retention_days', '1')
            self.logger = AWSLogger(
                log_group=aws_config.get('log_group', 'default-log-group'),
                log_stream=aws_config.get('log_stream', 'default-log-stream'),
                aws_region=aws_config.get('region', 'us-west-2')
            )
        elif environment == 'gcp':
            gcp_config = config.get('gcp', {})
            self.logger = GCPLogger(
                log_name=gcp_config.get('log_name', 'default-log'),
                project=gcp_config.get('project', 'default-project'),
                application_credentials=gcp_config.get('google_application_credentials')
            )
        else:
            local_config = config.get('local', {})
            self.logger = LocalLogger(
                log_file = local_config.get('log_file', 'default_local_log.log')
            )

        return self.logger


# Singleton instance of LoggerFactory
logger_factory = LoggerFactory2()


def log2(level: str, message: str):
    logger = logger_factory.get_logger()
    logger.log(level, message)
