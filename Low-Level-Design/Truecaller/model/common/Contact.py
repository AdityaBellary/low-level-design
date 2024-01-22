from dataclasses import dataclass

@dataclass
class Contact:
    phone: str
    countryCode: str = None
    email: str = None
