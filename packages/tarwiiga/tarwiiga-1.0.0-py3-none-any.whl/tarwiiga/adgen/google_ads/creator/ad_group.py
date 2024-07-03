from .client import create_client


def create_ad_group(name, campaign_id, account_id):
    client = create_client()

    ad_group_service = client.get_service("AdGroupService")
    campaign_service = client.get_service("CampaignService")

    ad_group_operation = client.get_type("AdGroupOperation")
    ad_group = ad_group_operation.create
    ad_group.name = name
    ad_group.status = client.enums.AdGroupStatusEnum.ENABLED
    ad_group.campaign = campaign_service.campaign_path(account_id, campaign_id)
    ad_group.type_ = client.enums.AdGroupTypeEnum.SEARCH_STANDARD
    ad_group.cpc_bid_micros = 10000000

    ad_group_response = ad_group_service.mutate_ad_groups(
        customer_id=account_id, operations=[ad_group_operation]
    )

    resource_name = ad_group_response.results[0].resource_name

    ad_group = {
        "ad_group_id": resource_name.split('/')[-1],
        "name": name,
        "resource_name": resource_name,
        "campaign_id": campaign_id,
        "account_id": account_id,
    }

    return ad_group


def get_ad_groups(account_id):
    ad_groups = []
    client = create_client()
    ga_service = client.get_service("GoogleAdsService")

    ad_groups_query = (
            "SELECT ad_group.id, ad_group.name, campaign.id " +
            "FROM ad_group " +
            "ORDER BY ad_group.id "
    )

    stream = ga_service.search_stream(
        customer_id=account_id,
        query=ad_groups_query,
    )
    for batch in stream:
        for row in batch.results:
            ad_group = {
                "ad_group_id": str(row.ad_group.id),
                "name": row.ad_group.name,
                "resource_name": row.ad_group.resource_name,
                "campaign_id": str(row.campaign.id),
                "account_id": account_id,
            }
            ad_groups.append(ad_group)
    return ad_groups

