from django.apps import AppConfig


class NeighbourhoodConfig(AppConfig):
    name = 'neighbourhood'
    def ready(self):
        import neighbourhood.signals