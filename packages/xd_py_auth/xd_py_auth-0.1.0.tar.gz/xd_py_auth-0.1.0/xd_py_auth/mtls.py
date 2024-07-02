from typing import Dict
from fastapi import FastAPI
import uvicorn


class Certificates:
    """
    A class to manage SSL/TLS certificate locations.
    """

    def __init__(self, certificate_location_dict: Dict[str, str]):
        """
        Initialize the Certificates object with certificate locations.

        Args:
            certificate_location_dict (Dict[str, str]): A dictionary mapping certificate types to their file paths.
        """
        for key, val in certificate_location_dict.items():
            setattr(self, key, val)

    def to_dict(self) -> Dict[str, str]:
        """
        Convert the certificate locations to a dictionary.

        Returns:
            Dict[str, str]: A dictionary of certificate locations.
        """
        return dict(self.__dict__)

    def __repr__(self) -> str:
        """
        Return a string representation of the Certificates object.

        Returns:
            str: A string representation of the certificate locations.
        """
        return str(self.to_dict())


class MTLSAuthenticationServer:
    """
    A class to manage an mTLS authenticated FastAPI server.
    """

    def __init__(self, app: FastAPI):
        """
        Initialize the MTLSAuthenticationServer.

        Args:
            app (FastAPI): The FastAPI application instance.
        """
        self.app = app
        self.certificates: Certificates | None = None

    def get_certificate(self) -> Dict[str, str]:
        """
        Get the current certificate locations.

        Returns:
            Dict[str, str]: A dictionary of certificate locations.

        Raises:
            AttributeError: If certificates have not been set.
        """
        if self.certificates is None:
            raise AttributeError("Certificates have not been set.")
        return self.certificates.to_dict()

    def set_certificate(self, certificate: Certificates) -> None:
        """
        Set the certificates for the server.

        Args:
            certificate (Certificates): A Certificates object containing certificate locations.
        """
        self.certificates = certificate

    def start(self) -> None:
        """
        Start the FastAPI server with mTLS authentication.

        Raises:
            AttributeError: If certificates have not been set.
        """
        if self.certificates is None:
            raise AttributeError(
                "Certificates must be set before starting the server."
            )

        uvicorn.run(
            self.app,
            host="0.0.0.0",
            port=8000,
            ssl_certfile=self.certificates.ssl_certfile,
            ssl_keyfile=self.certificates.ssl_keyfile,
            ssl_ca_certs=self.certificates.ssl_ca_certs,
        )