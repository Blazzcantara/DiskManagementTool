import logging

class DiskToolError(Exception):
    pass

class AnalysisError(DiskToolError):
    pass

# Add other error classes here

def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except DiskToolError as e:
            logging.error(f"An error occurred: {str(e)}")
            return None
        except Exception as e:
            logging.critical(f"An unexpected error occurred: {str(e)}")
            raise
    return wrapper
