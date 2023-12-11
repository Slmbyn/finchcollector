from django.forms import ModelForm
from .models import Feeding

# Creating a custom ModelForm:

class FeedingForm(ModelForm):
  class Meta:
    # declaring the Model being used
    model = Feeding
    # the fields we want inputs generated for
    fields = ['date', 'meal']