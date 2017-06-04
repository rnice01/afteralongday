from django.forms import ModelForm
from django.forms.widgets import Textarea, TextInput
from .models import Testimonial
from django.utils.translation import ugettext_lazy as _

class CreateTestimonialForm(ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'feedback']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control'
            }),
            'feedback': Textarea(attrs={
                'id': 'testimonial_feedback',
                'class': 'form-control',
                'rows': 2})
        }

