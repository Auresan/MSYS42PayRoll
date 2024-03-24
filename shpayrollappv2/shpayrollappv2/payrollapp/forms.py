from django import forms

class UploadAttendanceForm(forms.Form):
    csv_file = forms.FileField(label='Select a CSV file', help_text='Only CSV files are allowed.')