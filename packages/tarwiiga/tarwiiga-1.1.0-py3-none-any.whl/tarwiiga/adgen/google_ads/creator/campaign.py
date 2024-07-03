import sys
from .client import create_client
from google.ads.googleads.errors import GoogleAdsException


def create_budget(name, amount, account_id):
    client = create_client()

    campaign_budget_service = client.get_service("CampaignBudgetService")
    campaign_budget_operation = client.get_type("CampaignBudgetOperation")
    campaign_budget = campaign_budget_operation.create
    campaign_budget.name = name
    campaign_budget.delivery_method = client.enums.BudgetDeliveryMethodEnum.STANDARD
    campaign_budget.amount_micros = amount * 1000000

    try:
        campaign_budget_response = (
            campaign_budget_service.mutate_campaign_budgets(
                customer_id=account_id,
                operations=[campaign_budget_operation]
            )
        )
    except GoogleAdsException as ex:
        handle_googleads_exception(ex)

    budget = {
        "budget_id": campaign_budget_response.results[0].resource_name.split('/')[-1],
        "name": name,
        "amount": amount,
        "resource_name": campaign_budget_response.results[0].resource_name,
        "account_id": account_id
    }

    return budget


def create_campaign(name, budget, account_id):
    client = create_client()

    campaign_service = client.get_service("CampaignService")
    campaign_operation = client.get_type("CampaignOperation")
    campaign = campaign_operation.create
    campaign.name = name

    campaign.advertising_channel_type = client.enums.AdvertisingChannelTypeEnum.SEARCH
    campaign.network_settings.target_google_search = True
    campaign.network_settings.target_search_network = False
    campaign.network_settings.target_partner_search_network = False
    campaign.network_settings.target_content_network = False

    campaign.campaign_budget = budget["resource_name"]
    campaign.manual_cpc.enhanced_cpc_enabled = True

    try:
        campaign_response = campaign_service.mutate_campaigns(
            customer_id=account_id,
            operations=[campaign_operation]
        )
    except GoogleAdsException as ex:
        handle_googleads_exception(ex)

    resource_name = campaign_response.results[0].resource_name

    campaign = {
        "campaign_id": resource_name.split('/')[-1],
        "name": name,
        "resource_name": resource_name,
        "account_id": account_id,
    }

    return campaign


def get_campaigns(account_id):
    campaigns = []
    client = create_client()
    ga_service = client.get_service("GoogleAdsService")

    campaigns_query = (
            "SELECT campaign.id, campaign.name " +
            "FROM campaign " +
            "ORDER BY campaign.id "
    )

    stream = ga_service.search_stream(
        customer_id=account_id,
        query=campaigns_query,
    )
    for batch in stream:
        for row in batch.results:
            campaign = {
                "campaign_id": row.campaign.id,
                "name": row.campaign.name,
                "resource_name": row.campaign.resource_name,
                "account_id": account_id
            }
            campaigns.append(campaign)
    return campaigns


def handle_googleads_exception(exception):
    print(
        f'Request with ID "{exception.request_id}" failed with status '
        f'"{exception.error.code().name}" and includes the following errors:'
    )
    for error in exception.failure.errors:
        print(f'\tError with message "{error.message}".')
        if error.location:
            for field_path_element in error.location.field_path_elements:
                print(f"\t\tOn field: {field_path_element.field_name}")
    sys.exit(1)

