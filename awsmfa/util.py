import sys


def log_error_and_exit(logger, message):
    """Log an error message and exit with error"""
    logger.error(message)
    sys.exit(1)


def prompter():
    try:
        # PyLint will complain if unresolved
        console_input = raw_input  # type: ignore
    except NameError:
        # PyLint will complain if unresolved
        console_input = input  # type: ignore

    return console_input
