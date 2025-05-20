from typing import Optional, Union, Dict, List, Literal
from pydantic import BaseModel, Field, constr, conlist, condecimal, model_validator
import pycountry 

from typing_extensions import Annotated
import re

# Chaîne courte (entre 1 et 64 caractères)
ShortStr = Annotated[str, Field(min_length=1, max_length=64)]

# Numéro de rue : chaîne coercible correspondant à un nombre suivi éventuellement d'une lettre
StreetNumberStr = Annotated[
    str,
    Field(pattern=r'^\d+[a-z]?$')
]

class Address(BaseModel):
    street: str
    number: StreetNumberStr

class School(BaseModel):
    name: str
    address: Address

class ModuleDetails(BaseModel):
    name: str
    courses: List[str]

class Country(BaseModel):
    code: str
    name: str
    alpha_3: Optional[str] = None
    numeric: Optional[str] = None
    phone_code: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def parse_input(cls, value):
        if isinstance(value, cls):
            return value  # déjà une instance valide

        if not isinstance(value, str):
            raise TypeError("Country must be provided as a string or Country instance")

        try:
            country = pycountry.countries.lookup(value)
        except LookupError:
            raise ValueError(f"Invalid country name or code: '{value}'")

        # Récupération de l'indicatif via phonenumbers (optionnel)
        phone_code = None
        try:
            from phonenumbers.data import _country_code_to_region_code
            code_map = {v: k for k, vs in _country_code_to_region_code.items() for v in vs}
            dial = code_map.get(country.alpha_2)
            if dial:
                phone_code = f"+{dial}"
        except Exception:
            pass

        return dict(
            code=country.alpha_2,
            name=country.name,
            alpha_3=getattr(country, 'alpha_3', None),
            numeric=getattr(country, 'numeric', None),
            phone_code=phone_code
        )

class Person(BaseModel):
    firstname: str
    lastname: str
    country: Country
