from django import forms

class CancelForm(forms.Form):
    reason = forms.CharField(
        label='Reason for cancellation',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        required=True,
        help_text='Please provide a reason for your cancellation.'
    )