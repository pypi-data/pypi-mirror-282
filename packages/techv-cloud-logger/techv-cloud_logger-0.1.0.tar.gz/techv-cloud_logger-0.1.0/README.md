# Cloud Logger

A logger implementation for AWS, GCP, and local logging.

## Installation

```bash
pip install cloud_logger

## Usage

loud_logger import LoggerFactory

# Get logger instance
logger = LoggerFactory.get_logger()
logger.log("info", "This is a test log message")
logger.log("error", "This is an error message")
