"""
Custom Logging Module

This module provides a custom logging solution with colored output for different log levels.
It uses the standard Python logging module along with colorama for terminal color support.

Classes:
- ColoredFormatter: A custom logging formatter that adds color to log messages.
- Logger: A wrapper class for creating and configuring loggers with colored output.

Dependencies:
- logging: Standard Python logging module.
- os: For file path operations.
- datetime: For timestamp formatting.
- colorama: For adding colors to terminal output.

Usage:
    logger = Logger("MyLogger").get_logger()
    logger.info("This is an info message")
    logger.error("This is an error message")
"""

import logging
import os
from datetime import datetime
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

class ColoredFormatter(logging.Formatter):
    """
    A custom logging formatter class that adds color to log messages based on their level.

    This formatter customizes the appearance of log messages by adding color codes
    and formatting the log string with additional information such as timestamp,
    file name, and function name.

    Attributes:
        COLORS (dict): A dictionary mapping log levels to color codes.
    """

    COLORS = {
        'DEBUG': Fore.CYAN,
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.RED + Back.WHITE
    }

    def format(self, record):
        """
        Formats the log record with color and additional information.

        Args:
            record (logging.LogRecord): The log record to be formatted.

        Returns:
            str: The formatted log string with color codes.

        The formatted string includes:
        - Log level (centered in 13 characters)
        - Date (YYYY-MM-DD)
        - Time (HH:MM:SS)
        - File name (basename of the file where the log was called)
        - Class name (if available)
        - Function name
        - Log message

        Each log level is color-coded according to the COLORS dictionary.
        """
        log_fmt = f'[{record.levelname:^13}] '
        log_fmt += f'{datetime.fromtimestamp(record.created).strftime("%Y-%m-%d"):<11} '
        log_fmt += f'{datetime.fromtimestamp(record.created).strftime("%H:%M:%S"):<9} '
        log_fmt += f'{os.path.basename(record.pathname)} '
        
        if hasattr(record, 'class_name'):
            log_fmt += f'{record.class_name} '
        
        log_fmt += f'{record.funcName} '
        log_fmt += f'{record.getMessage()}'

        color = self.COLORS.get(record.levelname, '')
        return f'{color}{log_fmt}{Style.RESET_ALL}'

class Logger:
    """
    A wrapper class for creating and configuring loggers with colored output.

    This class simplifies the process of creating a logger with a ColoredFormatter
    and provides a method to retrieve the configured logger.

    Attributes:
        logger (logging.Logger): The underlying logger object.

    Methods:
        __init__(name): Initializes the Logger with a given name.
        _setup_handler(): Sets up the StreamHandler with ColoredFormatter.
        get_logger(): Returns the configured logger object.
    """

    def __init__(self, name):
        """
        Initializes a new Logger instance.

        Args:
            name (str): The name of the logger.

        This method creates a new logger, sets its level to DEBUG,
        and sets up a handler with the ColoredFormatter.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self._setup_handler()

    def _setup_handler(self):
        """
        Sets up a StreamHandler with ColoredFormatter for the logger.

        This method creates a StreamHandler, applies the ColoredFormatter to it,
        and adds the handler to the logger.
        """
        handler = logging.StreamHandler()
        handler.setFormatter(ColoredFormatter())
        self.logger.addHandler(handler)

    def get_logger(self):
        """
        Returns the configured logger object.

        Returns:
            logging.Logger: The configured logger object ready for use.
        """
        return self.logger