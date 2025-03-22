import logging
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)

def validate_positive_integer(value):
    """Ensures a value is a positive integer."""
    if not isinstance(value, int) or value < 0:
        raise ValidationError(f"Invalid value: {value}. Must be a positive integer.")

def log_request_info(request):
    """Logs essential request details."""
    logger.info(
        f"[{request.method}] {request.path} - User: {request.user} - Data: {request.body.decode('utf-8') if request.body else 'No Data'}"
    )