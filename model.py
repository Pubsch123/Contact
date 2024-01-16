from pydantic import BaseModel


# Defining the model


class Contact(BaseModel):
    name: str
    email: str
    phone1: str
    phone2: str