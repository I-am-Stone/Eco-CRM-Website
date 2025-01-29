from inventory.models import ContactForm


class ContactService:

    
    @classmethod
    def create(cls, email, name, subject, message):
        contact_message = ContactForm.objects.create(email=email, name=name, subject=subject, message=message)
        contact_message.save()

