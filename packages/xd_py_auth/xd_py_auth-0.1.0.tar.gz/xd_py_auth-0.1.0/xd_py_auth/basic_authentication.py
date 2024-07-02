import os
from typing import List
import re
import json
import hmac


class BasicAuthentication:
    def __init__(self, options=None):
        self.options = options or {"env": "development"}
        self.load_credentials()

    def load_credentials(self):
        current_dir = os.path.dirname(__file__)
        config_path = os.path.join(current_dir, "conf", "config.json")

        try:
            with open(config_path, "r") as f:
                config = json.load(f)
                self.stored_cred = config.get(self.options["env"], {}).get(
                    "user_credential", []
                )
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Config file not found at path: {config_path}"
            )

    def verify_user(self, username, password):
        if not username or not password:
            return False
        for user_credential in self.stored_cred:
            if hmac.compare_digest(
                username, user_credential["username"]
            ) and hmac.compare_digest(password, user_credential["password"]):
                return True
        return False

    def verify_token(self, token):
        if not token:
            return False
        for user_credential in self.stored_cred:
            if hmac.compare_digest(token, user_credential["zToken"]):
                return True
        return False


class CredentialsValidator:
    @staticmethod
    def check_password_length(value: str) -> None:
        if len(value) < 8:
            raise ValueError("Password length should be at least 8")
        if len(value) > 20:
            raise ValueError("Password length should not be greater than 20")

    @staticmethod
    def is_special_char(char: str) -> bool:
        special_chars: List[str] = [
            "$",
            "@",
            "#",
            "%",
            "!",
            "%",
            "^",
            "&",
            "*",
            "-",
            "_",
            ".",
            ",",
            ";",
            ":",
            "(",
            ")",
            "[",
            "]",
            "{",
            "}",
        ]
        return char in special_chars

    @staticmethod
    def check_password_criteria(value: str):
        criteria = [
            (str.isdigit, "Password should have at least one numeral"),
            (str.isupper, "Password should have at least one uppercase"),
            (str.islower, "Password should have at least one lowercase"),
            (
                CredentialsValidator.is_special_char,
                "Password should have at least one of the symbols",
            ),
        ]

        for criterion, error_message in criteria:
            if not any(criterion(char) for char in value):
                raise ValueError(error_message)

    @staticmethod
    def check_email_criteria(value: str):
        pattern = r"^[a-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, value):
            raise ValueError("Invalid email format")
        return value


class Validators(CredentialsValidator):
    @staticmethod
    def validate_email(value):
        return Validators.check_email_criteria(value)

    @staticmethod
    def validate_password(value: str) -> str:
        Validators.check_password_length(value)
        Validators.check_password_criteria(value)
        return value
