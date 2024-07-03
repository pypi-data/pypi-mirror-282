import datetime
import time
import requests
import json
from ..config import get_config


class QueryName:
    POST_CONTACT = "postContact"
    POSTS = "posts"


def get_url(query_name):
    config = get_config()
    base_url = config("SCRAPPER_BASE_URL")
    client_id = config("SCRAPPER_CLIENT_ID")
    version = config("SCRAPPER_VERSION")
    url = f"{base_url}?queryName={query_name}&clientId={client_id}&version={version}"
    return url


def get_query(query_name):
    query = ""
    if query_name == QueryName.POSTS:
        query = ("\n    query FetchAds($id: [Int] = null, $city: String = null, $cities: [String], "
                 "$authorUsername: String = null, $page: Int = null, $limit: Int = null, "
                 "$afterPostDate: Int = null, $afterUpdateDate: Int = null, $beforeUpdateDate: Int = null, "
                 "$beforePostDate: Int = null, $tag: String = null, $near: String = null, "
                 "$onlyWithImage: Boolean = null, $orderMainByPostId: Boolean = null, "
                 "$notTag: String = null) {\n  posts(\n    id: $id\n    city: $city\n    "
                 "cities: $cities\n    authorUsername: $authorUsername\n    page: $page\n    "
                 "limit: $limit\n    afterPostDate: $afterPostDate\n    afterUpdateDate: $afterUpdateDate\n    "
                 "beforeUpdateDate: $beforeUpdateDate\n    beforePostDate: $beforePostDate\n    tag: $tag\n    "
                 "near: $near\n    onlyWithImage: $onlyWithImage\n    orderMainByPostId: $orderMainByPostId\n    "
                 "notTag: $notTag\n  ) {\n    items {\n      ...PostFields\n    }\n    pageInfo {\n      "
                 "hasNextPage\n    }\n    viewOptions {\n      mustLoginToView\n    }\n  }\n}\n    \n    "
                 "fragment PostFields on Post {\n  id\n  title\n  postDate\n  updateDate\n  authorUsername\n  "
                 "authorId\n  URL\n  bodyTEXT\n  bodyHTML\n  thumbURL\n  hasImage\n  city\n  geoCity\n  "
                 "geoNeighborhood\n  geoHash\n  tags\n  imagesList\n  commentEnabled\n  commentStatus\n  "
                 "commentCount\n  upRank\n  downRank\n  status\n  postType\n  generalInfo {\n    key\n    "
                 "value\n  }\n  price {\n    formattedPrice\n  }\n  realEstateInfo {\n    "
                 "...realEstateOptions\n  }\n  carInfo {\n    sellOrWaiver\n    is4DW\n    "
                 "model\n    mileage\n    fuel\n    gear\n    carOrRelated\n    Bank\n  }\n  "
                 "tagsFilters\n  postNotesList {\n    iconName\n    iconUrl\n    note\n    link\n  }\n  "
                 "BuyButton {\n    Link\n    Name\n    StoreName\n  }\n}\n    \n    fragment "
                 "realEstateOptions on reInfo {\n  re_AdvertiserType\n  re_Direction\n  re_StreetType\n  "
                 "re_AccommType\n  re_IsKitchenIncluded\n  re_IsFurnished\n  re_IsDriverRoomAvilable\n  "
                 "re_IsMaidRoomAvilable\n  re_IsFireRoomAvilable\n  re_IsOutsideRoomAvilable\n  "
                 "re_IsCarGateAvilable\n  re_IsElevatorAvilable\n  re_IsParkingAvilable\n  "
                 "re_IsCellarIncludedAvilable\n  re_IsGardenAvilable\n  re_IsACIncludedAvilable\n  "
                 "re_IsPoolAvilable\n  re_IsVolleyBallAvilable\n  re_IsFootBallAvilable\n  "
                 "re_IsKidsGamesAvilable\n  re_IsStairInsideAvilable\n  re_IsYardAvilable\n  "
                 "re_IsBooked\n  re_Area\n  re_PropertyAge\n  re_StreetWide\n  re_RoomCount\n  "
                 "re_LivingRoomCount\n  re_WCCount\n  re_ApartmentCount\n  re_CheckInDate\n  "
                 "re_CheckOutDate\n  re_VillaCount\n  re_PlanNum\n  re_LandNum\n  re_MachineCount\n  "
                 "re_PalmCount\n  re_MeterPrice\n  re_FloorNum\n  re_REGA_Advertiser_registration_number\n  "
                 "re_REGA_Authorization_number\n  re_VillaType\n  re_IsOutdoorSessionsAvailable\n  "
                 "re_IsLivingRoomAvailable\n  re_IsTransformerAvailable\n  re_IsWCAvailable\n  "
                 "re_IsStageAvailable\n  re_IsStorehouseAvailable\n  re_IsWaterAvailable\n  "
                 "re_IsProtectoratesAvailable\n  re_IsElectricityAvailable\n  re_IsPrivateHallAvailable\n  "
                 "re_IsPrivateEntranceAvailable\n  re_IsWorkersHouseAvailable\n  re_IsTentHouseAvailable\n  "
                 "re_IsFoodHallAvailable\n  re_IsTwoDepartment\n  re_IsWaterTankAvailable\n  "
                 "re_IsPrivateHouseAvailable\n  re_IsBridalDepartmentAvailable\n  re_IsPlowAvailable\n  "
                 "re_IsGymAvailable\n  re_IsWaterSprinklerAvailable\n  re_TentCount\n  re_WellsCount\n  "
                 "re_HallsCount\n  re_FloorsCount\n  re_TentHouseCount\n  re_SessionsCount\n  re_ShopsCount\n  "
                 "re_SupportDailyRentSystem\n  re_SupportMonthlyRentSystem\n  re_SupportYearlyRentSystem\n}\n    ")
    elif query_name == QueryName.POST_CONTACT:
        query = ("query postContact($postId: Int!, $isManualRequest: Boolean) {\n    \n  "
                 "postContact(postId: $postId, isManualRequest: $isManualRequest)\n  { \n    "
                 "contactText\n    contactMobile\n }\n  \n  }")
    return query


def get_payload(
        query_name,
        page_number: int | None = None,
        tag: str | None = None,
        before: int | None = None,
        post_id: str | None = None
):
    query = get_query(query_name)
    payload = ""
    if query_name == QueryName.POSTS:
        payload = json.dumps({
            "query": query,
            "variables": {
                "isRe": True,
                "ids": [],
                "tag": tag,
                "page": page_number,
                "orderMainByPostId": False,
                "beforeUpdateDate": before
            }
        })
    elif query_name == QueryName.POST_CONTACT:
        payload = json.dumps({
            "query": query,
            "variables": {"postId": post_id, "isManualRequest": True}
        })
        return payload
    return payload


def get_headers(query_name):
    config = get_config()
    headers = {}
    if query_name == QueryName.POSTS:
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f'AWSALB={config("SCRAPPER_COOKIE_AWSALB")}; '
                      f'AWSALBCORS={config("SCRAPPER_COOKIE_AWSALB")}; '
                      f'AWSALBTG={config("SCRAPPER_COOKIE_AWSALBTG")}; '
                      f'AWSALBTGCORS={config("SCRAPPER_COOKIE_AWSALBTG")}'
        }
    elif query_name == QueryName.POST_CONTACT:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {config("SCRAPPER_AUTHORIZATION")}',
        }
    return headers


def scrape_phone_number(post_id):
    url = get_url(QueryName.POST_CONTACT)
    payload = get_payload(query_name=QueryName.POST_CONTACT, post_id=post_id)
    headers = get_headers(QueryName.POST_CONTACT)
    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    phone_number = data["data"]["postContact"]["contactMobile"]
    return phone_number


def scrape_posts(page_number, tag):
    current_time = datetime.datetime.now()
    current_timestamp = int(time.mktime(current_time.timetuple()))
    url = get_url(QueryName.POSTS)
    payload = get_payload(
        query_name=QueryName.POSTS,
        page_number=page_number,
        tag=tag,
        before=current_timestamp
    )
    headers = get_headers(QueryName.POSTS)
    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    posts = data["data"]["posts"]["items"]

    all_posts = []
    for post in posts:
        phone_number = scrape_phone_number(post["id"])
        if phone_number != "":
            post["phone_number"] = phone_number
            post["page_number"] = page_number
            post["tag"] = tag
            post["before"] = current_timestamp
            all_posts.append(post)

    return all_posts
