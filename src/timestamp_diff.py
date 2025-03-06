from datetime import datetime, timedelta
from typing import Union

def calculate_timestamp_difference(timestamp1: Union[str, datetime], 
                                   timestamp2: Union[str, datetime]) -> timedelta:
    """
    Calculate the time difference between two timestamps.

    Args:
        timestamp1 (Union[str, datetime]): First timestamp 
        timestamp2 (Union[str, datetime]): Second timestamp

    Returns:
        timedelta: Absolute time difference between the two timestamps

    Raises:
        ValueError: If timestamps are in invalid format
        TypeError: If input types are not supported
    """
    # Convert string timestamps to datetime objects if needed
    def parse_timestamp(ts):
        try:
            if isinstance(ts, str):
                # Try multiple common datetime formats
                formats = [
                    "%Y-%m-%d %H:%M:%S",  # Standard format
                    "%Y-%m-%dT%H:%M:%S",  # ISO format
                    "%Y-%m-%d",           # Date only
                    "%H:%M:%S"            # Time only
                ]
                
                for fmt in formats:
                    try:
                        return datetime.strptime(ts, fmt)
                    except ValueError:
                        continue
                
                # If no format matches
                raise ValueError(f"Unable to parse timestamp: {ts}")
            
            elif isinstance(ts, datetime):
                return ts
            
            else:
                raise TypeError(f"Unsupported timestamp type: {type(ts)}")
        
        except Exception as e:
            raise ValueError(f"Invalid timestamp format: {str(e)}")

    # Parse both timestamps
    dt1 = parse_timestamp(timestamp1)
    dt2 = parse_timestamp(timestamp2)

    # Calculate and return absolute time difference
    return abs(dt2 - dt1)