from google.ads.googleads.client import GoogleAdsClient
from ....config import get_config


def create_client():
    config = get_config()
    credentials = {
        "refresh_token": config("GOOGLE_ADS_REFRESH_TOKEN"),
        "client_id": config("GOOGLE_ADS_CLIENT_ID"),
        "client_secret": config("GOOGLE_ADS_CLIENT_SECRET"),
        "developer_token": config("GOOGLE_ADS_DEVELOPER_TOKEN"),
        "login_customer_id": config("GOOGLE_ADS_LOGIN_CUSTOMER_ID"),
        "use_proto_plus": config("GOOGLE_ADS_USE_PROTO_PLUS"),

    }
    client = GoogleAdsClient.load_from_dict(credentials)
    return client
