from django import forms


class CropWidget(forms.ClearableFileInput):
    template_name = 'widgets/crop_widget.html'

    class Media:
        css = {
            'all': ('staff/css/crop_widget.css',)
        }
        js = ('staff/js/CropWidget.js',)
