from django import forms
from .models import Diet
from patients.models import PatientProfile

class DietForm(forms.ModelForm):
    patient = forms.ModelChoiceField(
        queryset=PatientProfile.objects.all(),
        label="Paciente",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Diet
        fields = ['patient', 'name', 'meals', 'substitutions']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'meals': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Insira um JSON válido'}),
            'substitutions': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Insira um JSON válido (opcional)'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(DietForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['patient'].queryset = PatientProfile.objects.filter(
                nutritionist=user
            )
