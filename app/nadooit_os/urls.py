from django.urls import path

from nadooit_os.views import *

app_name = "nadooit_os"

urlpatterns = [
    path("", index_nadooit_os, name="nadooit-os"),
    path(
        "customer-time-account-overview",
        customer_time_account_overview,
        name="customer-time-account-overview",
    ),
    path(
        "orders-overview",
        customer_order_overview,
        name="customer-order-overview",
    ),
    path("create-api-key", create_api_key, name="create-api-key"),
    # Page to revoke API key their API key
    path("revoke-api-key", revoke_api_key, name="revoke-api-key"),
    path(
        "give-api-key-manager-role",
        give_api_key_manager_role,
        name="give-api-key-manager-role",
    ),
    path(
        "give-customer-time-account-manager-role",
        give_customer_time_account_manager_role,
        name="give-customer-time-account-manager-role",
    ),
]
