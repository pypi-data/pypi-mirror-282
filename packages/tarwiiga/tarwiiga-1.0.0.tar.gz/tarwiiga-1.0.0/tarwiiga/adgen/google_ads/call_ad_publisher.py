from .creator import create_client


def publish_call_ad(call_ad):
    client = create_client()
    googleads_service = client.get_service("GoogleAdsService")
    operation = client.get_type("AdGroupAdOperation")
    ad_group_ad = operation.create
    ad_group_ad.ad_group = googleads_service.ad_group_path(
        call_ad["account_id"],
        call_ad["ad_group_id"],
    )

    ad_group_ad.ad.call_ad.country_code = call_ad["country"]
    ad_group_ad.ad.call_ad.phone_number = call_ad["phone_number"]

    ad_group_ad.ad.final_urls.append(call_ad["final_url"])
    ad_group_ad.ad.call_ad.phone_number_verification_url = call_ad["final_url"]

    ad_group_ad.ad.call_ad.path1 = call_ad["path1"]
    ad_group_ad.ad.call_ad.path2 = call_ad["path2"]

    ad_group_ad.ad.call_ad.headline1 = call_ad["headline1"]
    ad_group_ad.ad.call_ad.headline2 = call_ad["headline2"]

    ad_group_ad.ad.call_ad.business_name = call_ad["business_name"]

    ad_group_ad.ad.call_ad.description1 = call_ad["description1"]
    ad_group_ad.ad.call_ad.description2 = call_ad["description2"]

    ad_group_ad_service = client.get_service("AdGroupAdService")
    response = ad_group_ad_service.mutate_ad_group_ads(
        customer_id=call_ad["account_id"],
        operations=[operation]
    )

    resource_name = response.results[0].resource_name

    call_ad["ad_id"] = resource_name.split('/')[-1].split('~')[-1]
    call_ad["resource_name"] = resource_name
    call_ad["manage_url"] = (f"https://ads.google.com/aw/ads"
                             f"?campaignId={call_ad['campaign_id']}"
                             f"&adGroupId={call_ad['ad_group_id']}")

    return call_ad
