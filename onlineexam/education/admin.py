from django.apps import apps
from django.contrib import admin


from django.db.models import BooleanField, ForeignKey, CharField, TextField
post_models = apps.get_app_config('education').get_models()

for model in post_models:
    model_name = model.__name__

    if model_name == 'User':
        continue  # Skip User model if needed

    try:
        search_fields = [
            field.name for field in model._meta.get_fields()
            if isinstance(field, (CharField, TextField)) and not isinstance(field, ForeignKey)
        ]

        # Set list filter (boolean fields only)
        list_filter = [
            field.name for field in model._meta.get_fields()
            if isinstance(field, BooleanField)
        ]

        # Create admin class dynamically
        class ModelAdmin(admin.ModelAdmin):
            search_fields = search_fields
            list_filter = list_filter

        admin.site.register(model, ModelAdmin)

    except admin.sites.AlreadyRegistered:
        pass
