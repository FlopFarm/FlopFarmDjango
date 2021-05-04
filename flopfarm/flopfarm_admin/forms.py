'''
Author: your name
Date: 2021-05-02 16:52:59
LastEditTime: 2021-05-04 12:55:44
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /FlopFarmDjango/flopfarm/flopfarm_admin/forms.py
'''
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _ 
class BuyInstanceForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.instance = kwargs.pop('instance', None)
        super(BuyInstanceForm, self).__init__(*args, **kwargs)

    expect_time = forms.FloatField(help_text="Enter the expected using time (in hour)")

    def clean_expect_time(self):
        data = self.cleaned_data['expect_time']
        if ((data == None) and (self.instance.type == 'c')):
            raise ValidationError(_('Invalid using time: the using time is required'))

        if (data <= 0):
            raise ValidationError(_('Invalid using time: the using time should be positive.'))

        return data