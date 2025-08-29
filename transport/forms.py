from django import forms
from .models import TravelOption
from merchant.models import Bus

class TravelOptionForm(forms.ModelForm):
    class Meta:
        model = TravelOption
        fields = [
            "type",
            "bus",
            "source",
            "destination",
            "date_time",
            "price",
            "available_seats",
            "repeat_days",
            "flight_number",
            "airline",
            "duration_minutes",
            "train_number",
            "coach_type",
        ]
        widgets = {
            "date_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "repeat_days": forms.TextInput(attrs={"placeholder": "Mon,Tue,Wed"}),
        }

    def __init__(self, *args, **kwargs):
        merchant = kwargs.pop("merchant", None)
        super().__init__(*args, **kwargs)
        if merchant:
            self.fields["bus"].queryset = Bus.objects.filter(merchant=merchant)

        # Hide bus if type != Bus
        if self.instance and self.instance.type != "Bus":
            self.fields["bus"].widget = forms.HiddenInput()
        # Hide flight fields if type != Flight
        if self.instance and self.instance.type != "Flight":
            self.fields["flight_number"].widget = forms.HiddenInput()
            self.fields["airline"].widget = forms.HiddenInput()
            self.fields["duration_minutes"].widget = forms.HiddenInput()
        # Hide train fields if type != Train
        if self.instance and self.instance.type != "Train":
            self.fields["train_number"].widget = forms.HiddenInput()
            self.fields["coach_type"].widget = forms.HiddenInput()


class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ["bus_number", "total_seats", "model_name"]
