import ftplib
from typing import Optional, Tuple

def establish_ftp_connection(
    host: str, 
    username: str, 
    password: str, 
    port: int = 21, 
    timeout: int = 30
) -> Tuple[Optional[ftplib.FTP], Optional[str]]:
    """
    Establish a connection to an FTP server.

    Args:
        host (str): The FTP server hostname or IP address.
        username (str): Username for FTP authentication.
        password (str): Password for FTP authentication.
        port (int, optional): Port number for FTP connection. Defaults to 21.
        timeout (int, optional): Connection timeout in seconds. Defaults to 30.

    Returns:
        Tuple[Optional[ftplib.FTP], Optional[str]]: 
        - A tuple containing the FTP connection object if successful, 
          or None if connection fails
        - An error message if connection fails, or None if successful
    """
    try:
        # Validate input parameters
        if not host:
            return None, "Host cannot be empty"
        
        if not username:
            return None, "Username cannot be empty"
        
        if not password:
            return None, "Password cannot be empty"
        
        # Establish FTP connection
        ftp = ftplib.FTP()
        ftp.connect(host=host, port=port, timeout=timeout)
        
        # Attempt to login
        ftp.login(user=username, passwd=password)
        
        return ftp, None
    
    except ftplib.all_errors as e:
        # Catch and return any FTP-related errors
        return None, f"FTP Connection Error: {str(e)}"
    except Exception as e:
        # Catch any unexpected errors
        return None, f"Unexpected Error: {str(e)}"