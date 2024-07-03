from ....config import get_config
from .client import create_client


def create_account(name, currency, time_zone, manager_id):
    client = create_client()
    service = client.get_service("CustomerService")

    customer = client.get_type("Customer")
    customer.descriptive_name = name
    customer.currency_code = currency
    customer.time_zone = time_zone

    customer_response = service.create_customer_client(
        customer_id=manager_id,
        customer_client=customer,
    )

    resource_name = customer_response.resource_name

    account = {
        "account_id": resource_name.split('/')[-1],
        "name": name,
        "time_zone": time_zone,
        "currency": currency,
        "resource_name": resource_name,
        "manager": False,
        "manager_id": manager_id,
    }

    return account


def get_all_accounts():
    config = get_config()

    client = create_client()

    accounts = []
    googleads_service = client.get_service("GoogleAdsService")

    accounts_query = (
            "SELECT "
            "customer_client.client_customer, "
            "customer_client.level, "
            "customer_client.manager, "
            "customer_client.descriptive_name, "
            "customer_client.currency_code, "
            "customer_client.time_zone, "
            "customer_client.id " +
            "FROM customer_client " +
            "WHERE customer_client.level <= 1 "
    )

    accounts_response = googleads_service.search(
        customer_id=config('GOOGLE_ADS_LOGIN_CUSTOMER_ID'),
        query=accounts_query
    )
    for account_item in accounts_response:
        customer_client = account_item.customer_client
        account = {
            "account_id": str(customer_client.id),
            "name": customer_client.descriptive_name,
            "time_zone": customer_client.time_zone,
            "currency": customer_client.currency_code,
            "resource_name": customer_client.resource_name,
            "manager": customer_client.manager,
        }
        if not customer_client.manager:
            account["manager_id"] = customer_client.resource_name.split('/')[1]
        else:
            account["manager_id"] = None
        accounts.append(account)
    return accounts


def get_manager_accounts():
    manager_accounts = []
    accounts = get_all_accounts()
    for account in accounts:
        if account["manager"]:
            manager_accounts.append(account)
    return manager_accounts


def get_sub_accounts(manager_id):
    sub_accounts = []
    accounts = get_all_accounts()
    for account in accounts:
        if "manager_id" in account and account["manager_id"] == manager_id:
            sub_accounts.append(account)
    return sub_accounts

