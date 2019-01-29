from rest_framework import routers

from shiplocation.views import ShipView, ShipLocationView

router = routers.SimpleRouter()
router.register(r'ships', ShipView)
router.register(r'positions', ShipLocationView)
urlpatterns = router.urls