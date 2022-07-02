from django.forms import widgets


class CropWidget(widgets.Widget):
    template_name = 'widgets/crop_widget.html'

    class Media:
        css = {
            'all': (
                'widgets/crop-widget/css/cropper.min.css',
                'widgets/crop-widget/css/crop-widget.css'
            )
        }
        js = (
            'widgets/crop-widget/js/cropper.min.js',
            'widgets/crop-widget/js/CropWidget.js'
        )
