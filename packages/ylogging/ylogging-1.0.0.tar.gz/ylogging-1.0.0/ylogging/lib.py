from datetime import datetime
import pytz

def get_structured_log_msg(
    context: str, message: str, serialized_data: str | None
) -> dict:
    """
    Logs a structured message to the console.
    """
    utc = pytz.UTC
    now = datetime.now(utc)
    log_msg_dict = {
        "context": context,
        "message": message,
        "serialized_data": serialized_data,
        "time": now.strftime("%Y-%m-%d %H:%M:%S"),
    }
    return log_msg_dict
