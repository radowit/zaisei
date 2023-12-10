from django.conf import settings
from django.contrib.sites.models import Site
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self) -> dict[str, Site]:
        context = super().get_context_data()
        context["site"] = Site.objects.get(id=settings.SITE_ID)
        return context
