__version__ = '1.0'

def log_status(log_file_path: str, component_name: str, status: str, message: str = ""):
    import os
    import json
    from datetime import datetime

    """Logs the status of a component to a file with a timestamp.

    :param log_file_path: path of file to log
    :param component_name: Name of the component
    :param status: Status of the component
    :param message: Additional message (optional)
    """
    log_entry = {
        "timestamp": str(datetime.utcnow()),
        "component": component_name,
        "status": status,
        "message": message
    }

    try:
        with open(log_file_path, "a+") as log_file:
            log_file.write(json.dumps(log_entry) + "\n")
            print(json.dumps(log_entry))
    except Exception as e:
        print(e)
