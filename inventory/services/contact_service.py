from inventory.models import ContactForm


class ContactService:
    def __init__(self):
        self.model = ContactForm

    def create(self, email, name, subject, message):
        contact_message = self.model.objects.create(email=email, name=name, subject=subject, message=message)
        contact_message.save()

