from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes




class ShopViewSet(viewsets.ModelViewSet):
	def list(self, request):
        pass
    @permission_classes((IsAdminUser,))
    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass
    
    @permission_classes((IsAdminUser,))
    def update(self, request, pk=None):
        super(ShopViewSet, self)

    @permission_classes((IsAdminUser,))
    def partial_update(self, request, pk=None):
        pass
    
    @permission_classes((IsAdminUser,))
    def destroy(self, request, pk=None):
        pass