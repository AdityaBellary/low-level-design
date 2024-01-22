from dataclasses import dataclass

@dataclass
class Address:
    addressLine1: str
    addressLine2: str
    addressLine3: str
    street: str
    city: str
    state: str
    pincode: str
    country: str