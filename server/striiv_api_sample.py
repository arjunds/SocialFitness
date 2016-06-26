
import sys

import requests

from requests_oauthlib import OAuth1

verifier = sys.argv[1]
user_token = sys.argv[2]
user_token_secret = sys.argv[3]

base_url = "https://striiv-api-prod.appspot.com"
access_token_path = "/api/1/access_token"
activity_path_format = "/api/1/user/-/activities/start/{start_date}/end/{end_date}/json"

auth = OAuth1(
    'fyTLMquBHr9Jvh5h',
    client_secret='maG9ezkuMNCxDGxa',
    verifier=verifier,
    resource_owner_key=user_token,
    resource_owner_secret=user_token_secret,
    signature_method="PLAINTEXT"
)

access_token_response = requests.post(url=base_url + access_token_path, auth=auth).content
property_strings = access_token_response.split("&")
properties = {
    property_string.split("=")[0]: property_string.split("=")[1]
    for property_string in property_strings
}

auth = OAuth1(
    'fyTLMquBHr9Jvh5h',
    client_secret='maG9ezkuMNCxDGxa',
    resource_owner_key=properties["oauth_token"],
    resource_owner_secret=properties["oauth_token_secret"],
    signature_method="PLAINTEXT"
)

activity_path = activity_path_format.format(user_id=properties["striiv_user_id"], start_date="2016-06-26", end_date="2016-06-26")
activity_response = requests.get(url=base_url + activity_path, auth=auth)

print activity_response.content
