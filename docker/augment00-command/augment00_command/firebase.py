import json
import requests

GOOGLE_IDENTITY_URL = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyCustomToken"


class FirebaseConnection():


    def __init__(self, entity_uuid, api_key, custom_token_url):
        # api_key = "AIzaSyBDu9g23GF8eihQLAIyV2WHEMTCLctfXSY"

        self.entity_uuid
        self.api_key = api_key
        self.custom_token_url = custom_token_url


    def sign_in_with_custom_token(self, token):

        request_ref = "{}?key={0}".format(GOOGLE_IDENTITY_URL, self.api_key)
        headers = {"content-type": "application/json; charset=UTF-8"}
        data = json.dumps({"returnSecureToken": True, "token": token})
        request_object = requests.post(request_ref, headers=headers, data=data)
        return request_object.json()


    def refresh(self, refresh_token):
        request_ref = "https://securetoken.googleapis.com/v1/token?key={0}".format(self.api_key)
        headers = {"content-type": "application/json; charset=UTF-8"}
        data = json.dumps({"grantType": "refresh_token", "refreshToken": refresh_token})
        request_object = requests.post(request_ref, headers=headers, data=data)
        request_object_json = request_object.json()
        # handle weirdly formatted response
        user = {
            "userId": request_object_json["user_id"],
            "idToken": request_object_json["id_token"],
            "refreshToken": request_object_json["refresh_token"]
        }
        return user