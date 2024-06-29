class ContactInfo:

    def __init__(self, contact_name: str, phone: str, email: str):
        self.contact_name = contact_name
        self.phone = phone
        self.email = email

    def __str__(self):
        return self.contact_name
