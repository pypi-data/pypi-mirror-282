from dal import autocomplete
from django.utils.html import escape
from artd_promotion.models import Product


class ProductAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Product.objects.none()

        qs = Product.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs

    def get_result_label(self, result):
        return escape(result.name)

    def get_selected_result_label(self, result):
        return escape(result.name)
