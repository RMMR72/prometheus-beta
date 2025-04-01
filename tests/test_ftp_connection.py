import pytest
import ftplib
from unittest.mock import patch, MagicMock
from src.ftp_connection import establish_ftp_connection

class TestFTPConnection:
    def test_successful_connection(self):
        """Test successful FTP connection"""
        with patch('ftplib.FTP') as mock_ftp:
            # Setup mock FTP object
            mock_instance = MagicMock()
            mock_ftp.return_value = mock_instance
            
            # Call the function
            connection, error = establish_ftp_connection(
                host='test.server.com', 
                username='testuser', 
                password='testpass'
            )
            
            # Assertions
            assert connection is not None
            assert error is None
            mock_instance.connect.assert_called_once()
            mock_instance.login.assert_called_once()

    def test_empty_host(self):
        """Test connection with empty host"""
        connection, error = establish_ftp_connection(
            host='', 
            username='testuser', 
            password='testpass'
        )
        
        assert connection is None
        assert error == "Host cannot be empty"

    def test_empty_username(self):
        """Test connection with empty username"""
        connection, error = establish_ftp_connection(
            host='test.server.com', 
            username='', 
            password='testpass'
        )
        
        assert connection is None
        assert error == "Username cannot be empty"

    def test_empty_password(self):
        """Test connection with empty password"""
        connection, error = establish_ftp_connection(
            host='test.server.com', 
            username='testuser', 
            password=''
        )
        
        assert connection is None
        assert error == "Password cannot be empty"

    def test_connection_error(self):
        """Test FTP connection error handling"""
        with patch('ftplib.FTP') as mock_ftp:
            # Setup mock to raise an error
            mock_instance = MagicMock()
            mock_ftp.return_value = mock_instance
            mock_instance.connect.side_effect = ftplib.error_perm("Connection failed")
            
            # Call the function
            connection, error = establish_ftp_connection(
                host='test.server.com', 
                username='testuser', 
                password='testpass'
            )
            
            # Assertions
            assert connection is None
            assert "FTP Connection Error" in error

    def test_custom_port(self):
        """Test connection with custom port"""
        with patch('ftplib.FTP') as mock_ftp:
            # Setup mock FTP object
            mock_instance = MagicMock()
            mock_ftp.return_value = mock_instance
            
            # Call the function with custom port
            connection, error = establish_ftp_connection(
                host='test.server.com', 
                username='testuser', 
                password='testpass',
                port=2121
            )
            
            # Assertions
            assert connection is not None
            assert error is None
            mock_instance.connect.assert_called_with(
                host='test.server.com', 
                port=2121, 
                timeout=30
            )