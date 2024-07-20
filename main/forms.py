from django import forms
from .models import Rating

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating', 'comments', 'professor']
        widgets = {'professor': forms.HiddenInput()}  # Hide professor field in form

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if not 1 <= rating <= 5:
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating
    

