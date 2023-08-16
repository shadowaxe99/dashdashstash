import logging


def handle_error(error):
    logging.error(str(error))
    # Additional error handling logic


if __name__ == '__main__':
    try:
        # Code that may raise an error
        raise ValueError('An error occurred')
    except Exception as e:
        handle_error(e)