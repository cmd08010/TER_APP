from django import forms

from .models import Register


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = [
            'register_type',
            'member_name',
            'account_address',
            'account_number',
            'member_email',
            'member_phone',
            'ven_id',
            'device_id',
            'device_type',
            'company',
            'aggregator_name',
            'aggregator_email',
            'aggregator_phone',
        ]
