from django.template import loader
from django.db import models
from django import forms

class EditorJsWidget(forms.widgets.Textarea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def media(self):
        return forms.Media(
            css = {
                "all": [
                    "simple-editorjs/main.css",
                ]
            },
            js = [
                "simple-editorjs/tools/header.js",
                "simple-editorjs/tools/simple-image.js",
                "simple-editorjs/tools/delimiter.js",
                "simple-editorjs/tools/list.js",
                "simple-editorjs/tools/checklist.js",
                "simple-editorjs/tools/quote.js",
                "simple-editorjs/tools/code.js",
                "simple-editorjs/tools/embed.js",
                "simple-editorjs/tools/table.js",
                "simple-editorjs/tools/link.js",
                "simple-editorjs/tools/warning.js",
                "simple-editorjs/tools/marker.js",
                "simple-editorjs/tools/inline-code.js",
                "simple-editorjs/main.js",
            ],
        )
    
    def render(self, name, value, **kwargs):
        return loader.render_to_string("simple-editorjs/main.html", {"name": name, "id": kwargs["attrs"]["id"], "value": value })

class EditorJsField(models.Field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_internal_type(self):
        return "TextField"
    
    def formfield(self, *args, **kwargs):
        kwargs["widget"] = EditorJsWidget()
        return super().formfield(*args, **kwargs)