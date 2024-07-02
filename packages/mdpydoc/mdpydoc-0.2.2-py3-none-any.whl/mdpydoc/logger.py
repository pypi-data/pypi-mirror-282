import logging
import colorlog
import inspect
from typing import Optional, Callable, Union
from functools import wraps
from pathlib import Path

class AppLogger:
    """
    AppLogger is a versatile logger class that can use either the standard logging library
    or the loguru library for enhanced logging. It supports colored output, automatic inclusion
    of class and function names in log messages, and concurrent logging with log rotation.

    Attributes:
        logger (Union[logging.Logger, loguru.Logger]): The underlying logger instance.

    Example:
        logger = AppLogger(logger_type="loguru").get_logger()
        logger.info("This is an info message")

    Note:
        The choice between standard logging and loguru affects the available methods and behavior.
        Refer to the respective library documentation for detailed usage.

    TODO:
        - Add support for custom log formats.
        - Implement log filtering capabilities.
        - Add support for remote logging (e.g., to a centralized log server).
    """

    def __init__(self, name: Optional[str] = None, level: int = logging.DEBUG, logger_type: str = "standard") -> None:
        """
        Initialize the AppLogger with the specified name, logging level, and logger type.

        Args:
            name (str, optional): The name of the logger. Defaults to the caller's module name.
            level (int): The logging level (e.g., logging.DEBUG, logging.INFO). Defaults to logging.DEBUG.
            logger_type (str): The type of logger to use ("standard" or "loguru"). Defaults to "standard".

        Raises:
            ValueError: If an invalid logger_type is provided.
        """
        if name is None:
            name = self._get_caller_module_name()

        if logger_type not in ["standard"]:
            raise ValueError("Invalid logger_type. Choose 'standard' or 'loguru'.")

        self._logger_instance = StandardAppLogger(name=name, level=level)
        
        self.logger = self._logger_instance.get_logger()
        self.logger.debug(f"AppLogger initialized with type: {logger_type}")

    def _get_caller_module_name(self) -> str:
        """
        Get the name of the module that called the AppLogger.

        Returns:
            str: The name of the caller's module.
        """
        frame = inspect.stack()[2]
        module = inspect.getmodule(frame[0])
        return module.__name__ if module else "__main__"

    def get_logger(self) -> Union[logging.Logger, loguru.Logger]:
        """
        Get the underlying logger instance.

        Returns:
            Union[logging.Logger, loguru.Logger]: The logger instance.
        """
        return self.logger

    def __getattr__(self, name: str) -> Callable:
        """
        Delegate attribute access to the underlying logger instance.

        Args:
            name (str): The attribute name to access.

        Returns:
            Callable: The attribute from the underlying logger instance.

        Raises:
            AttributeError: If the attribute is not found in the underlying logger.
        """
        try:
            return getattr(self._logger_instance, name)
        except AttributeError:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")


class StandardAppLogger:
    """
    StandardAppLogger is a custom logger class that uses the standard logging library.
    It supports colored output and automatic inclusion of class and function names in log messages.

    Attributes:
        logger (logging.Logger): The underlying standard logger instance.

    Note:
        This class is designed to be used internally by AppLogger.

    TODO:
        - Implement file-based logging with rotation similar to LoguruAppLogger.
        - Add support for custom log handlers.
    """

    def __init__(self, name: str, level: int = logging.DEBUG) -> None:
        """
        Initialize the StandardAppLogger with the specified name and logging level.

        Args:
            name (str): The name of the logger.
            level (int): The logging level (e.g., logging.DEBUG, logging.INFO). Defaults to logging.DEBUG.
        """
        self.logger = logging.getLogger(name)
        handler = colorlog.StreamHandler()
        formatter = colorlog.ColoredFormatter(
            '%(log_color)s%(levelname)s: %(asctime)s - %(name)s - %(class_name)s.%(func_name)s - %(message)s',
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            },
            datefmt='%Y-%m-%d %H:%M:%S',
            style='%'
        )
        handler.setFormatter(formatter)
        if not self.logger.handlers:
            self.logger.addHandler(handler)
        self.logger.setLevel(level)
        self.enhance_logger()

    def enhance_logger(self) -> None:
        """
        Enhances the logger to automatically include 'class_name' and 'func_name' in every log message.
        """
        def create_log_method(level: str) -> Callable:
            original_log_method = getattr(self.logger, level)

            @wraps(original_log_method)
            def log_method(message: str, *args, **kwargs) -> None:
                frame = inspect.stack()[1]
                class_name = frame.frame.f_locals.get('self', type('', (), {})).__class__.__name__
                if class_name == type.__name__:  # If called from a non-class context
                    class_name = 'global'
                function_name = frame.function
                if 'extra' not in kwargs:
                    kwargs['extra'] = {}
                kwargs['extra'].update({'class_name': class_name, 'func_name': function_name})
                original_log_method(message, *args, **kwargs)

            return log_method

        for level in ('debug', 'info', 'warning', 'error', 'critical'):
            setattr(self.logger, level, create_log_method(level))

    def get_logger(self) -> logging.Logger:
        """
        Get the underlying logger instance.

        Returns:
            logging.Logger: The logger instance.
        """
        return self.logger

# Example usage:
if __name__ == "__main__":
    # Standard logger
    std_logger = AppLogger(name="StandardLogger", logger_type="standard").get_logger()
    std_logger.info("This is an info message using standard logger")
    std_logger.debug("This is a debug message using standard logger")

    # Loguru logger
    loguru_logger = AppLogger(name="LoguruLogger", logger_type="loguru").get_logger()
    loguru_logger.info("This is an info message using loguru logger")
    loguru_logger.debug("This is a debug message using loguru logger")