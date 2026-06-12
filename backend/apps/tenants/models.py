from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

# Create your models here.
class Client(TenantMixin):
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    # auto_drop_schema = True  # Opcional: si borras el cliente, borra su esquema de la BD
    auto_create_schema = True  # Al crear el cliente, Django creará automáticamente su Schema privado
    paid_until = models.DateField()
    on_trial = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Domain(DomainMixin):
    pass