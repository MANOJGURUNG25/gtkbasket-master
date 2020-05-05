from django.urls import path
from .views import item_list, index,rice,pulses,oil,dry_fruits,Ghee,spice,sugar

app_name = 'website'

urlpatterns = [
    path('', item_list, name="item_list"),
    path('index/',index, name="index"),
    path('rice/',rice, name="rice"),
    path('pulses/',pulses, name="pulses"),
    path('oil/',oil, name="oil"),
    path('dry_fruits/',dry_fruits, name="dry_fruits"),
    path('Ghee/',Ghee, name="Ghee"),
    path('spice/',spice, name="spice"),
    path('sugar/',sugar, name="sugar"),
]
