from django.utils.module_loading import import_string

from openwisp_notifications import settings as app_settings


class IgnoreObjectNotificationWidgetMedia:
    extend = True
    js = (
        'admin/js/jquery.init.js',
        'openwisp-notifications/js/object-notifications.js',
    )
    css = {'all': ('openwisp-notifications/css/object-notifications.css',)}


def _add_object_notification_widget():
    """
    Adds object notification widget on configured ModelAdmins.
    """
    for model_admin_path in app_settings.IGNORE_ENABLED_ADMIN:
        model_admin_class = import_string(model_admin_path)
        try:
            if isinstance(model_admin_class.Media.js, list):
                model_admin_class.Media.js.extend(
                    IgnoreObjectNotificationWidgetMedia.js
                )
            elif isinstance(model_admin_class.Media.js, tuple):
                model_admin_class.Media.js += IgnoreObjectNotificationWidgetMedia.js

            if 'all' in model_admin_class.Media.css:
                if isinstance(model_admin_class.Media.css['all'], list):
                    model_admin_class.Media.css['all'].extend(
                        IgnoreObjectNotificationWidgetMedia.css['all']
                    )
                elif isinstance(model_admin_class.Media.css['all'], tuple):
                    model_admin_class.Media.css[
                        'all'
                    ] += IgnoreObjectNotificationWidgetMedia.css['all']
            else:
                model_admin_class.Media.css.update(
                    IgnoreObjectNotificationWidgetMedia.css
                )
        except AttributeError:
            model_admin_class.Media = IgnoreObjectNotificationWidgetMedia
