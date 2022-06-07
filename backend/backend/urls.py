from django.contrib import admin
from django.urls import include, path
from rest_framework import schemas
from rest_framework.response import Response
from rest_framework_simplejwt import views as jwt_views
from rest_framework.decorators import api_view, renderer_classes
from users.views import services_list, service_detail, service_companies
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer


@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Company cleaning API')
    return Response(generator.get_schema(request=request))


urlpatterns = [
    path('', schema_view),
    path('admin/', admin.site.urls),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path("users/", include("users.urls")),
    path("requests/", include("service_requests.urls")),
    path("offers/", include("offers.urls")),

    path("services/", services_list, name = "services"),
    path("services/<int:pk>/", service_detail, name = "service_detail"),
    path("services/<int:pk>/companies/", service_companies, name = "service_companies"),

    path('__debug__/', include('debug_toolbar.urls')),
]
