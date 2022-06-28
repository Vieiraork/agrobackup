from statistics import mode
from django.contrib.gis.db import models
from django.utils.translation import gettext as _

from farm_base.models.owner import Owner


class Farm(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=255,
                            null=True, blank=True)

    geometry = models.GeometryField(verbose_name=_("Geometry"),
                                    null=True, blank=True)

    area = models.FloatField(verbose_name=_("Area"),
                             blank=True, null=True)

    centroid = models.PointField(verbose_name=_("Centroid"),
                                 blank=True, null=True)

    creation_date = models.DateTimeField(verbose_name=_("Creation date"),
                                         auto_now_add=True, editable=False)
    
    municipality = models.CharField(verbose_name=_("Municipaly"), max_length=80, 
                                    blank=True, null=True)

    state = models.CharField(verbose_name=_("State"), max_length=80,
                            null=True, blank=True)

    last_modification_date = models.DateTimeField(
        verbose_name=_("Last modification date"), auto_now=True)

    is_active = models.BooleanField(verbose_name=_("Is Active"), default=True)

    owner = models.ForeignKey(Owner, related_name='owner', 
                            on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['id']
        verbose_name = _('Farm')
        verbose_name_plural = _('Farms')
