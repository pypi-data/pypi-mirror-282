from pybis import Openbis


class OpenbisImportError(Exception):
    """Custom exception for errors during the OpenBIS import process."""

    pass


class OpenbisConnectionError(OpenbisImportError):
    """Custom exception for connection errors with the OpenBIS server."""

    pass


class OpenbisLoginError(OpenbisImportError):
    """Custom exception for login errors with the OpenBIS server."""

    pass


class OpenbisHandler:
    """
    Context manager for handling interactions with the OpenBIS server.
    Ensures proper setup, login, and teardown.

    Attributes:
        project_url (str): The URL of the OpenBIS project.
        username (str): The username for OpenBIS login.
        password (str): The password for OpenBIS login.
        archive (str): The archive path.
        logger (logging.Logger): Logger for error and info messages.
    """

    def __init__(self, project_url, username, password, archive, logger):  # noqa: PLR0913
        self.project_url = project_url
        self.username = username
        self.password = password
        self.archive = archive
        self.logger = logger
        self.openbis = None
        self.spaces = []

    def __enter__(self):
        """
        Enter the runtime context related to this object.
        Initializes and logs into the OpenBIS server.

        Returns:
            self: An instance of the context manager.
        """
        try:
            self.openbis = Openbis(self.project_url, verify_certificates=False)
        except Exception as e:
            raise OpenbisConnectionError(
                f'Failed to connect to the OpenBIS server at {self.project_url}.'
            ) from e

        try:
            self.openbis.login(self.username, self.password, save_token=True)
        except Exception as e:
            raise OpenbisLoginError(
                'Failed to login to the OpenBIS server with the provided credentials.'
            ) from e

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exit the runtime context related to this object. Logs out the OpenBIS server.

        Args:
            exc_type (type): The exception type.
            exc_value (Exception): The exception instance.
            traceback (traceback): The traceback object.

        Returns:
            bool: False to propagate the exception, True to suppress it.
        """
        if self.openbis:
            try:
                self.openbis.logout()
            except Exception as e:
                self.logger.error(
                    'Failed to logout from the OpenBIS server.', exc_info=e
                )

        if exc_type is not None:
            self.logger.error(
                'An error occurred', exc_info=(exc_type, exc_value, traceback)
            )

        return False  # Propagate the exception if any
