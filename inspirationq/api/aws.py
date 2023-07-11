from .bare import iQBareAPI
import boto3
import time
import json


class iQAWSAPI(iQBareAPI):
    def __init__(self, username=None, password=None, base_url=None):
        super().__init__(base_url=base_url, group="aws")
        self.username = self.configuration_value("username", username)
        self.password = self.configuration_value("password", password)
        self.app_id = self.configuration_value("app_id", "7pjemis07hpeq8rvkqs02sstp3")
        self.region_name = self.configuration_value("region_name", "us-east-1")
        self.access_token = None

    def get_token_(self):
        client = boto3.client("cognito-idp", region_name=self.region_name)

        # Initiating the Authentication,
        response = client.initiate_auth(
            ClientId=self.app_id,
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={"USERNAME": self.username, "PASSWORD": self.password},
        )
        # Getting the user details.
        if "AuthenticationResult" in response:
            result = response["AuthenticationResult"]
            if "IdToken" in result:
                self.access_token = result["IdToken"]
                return True
        raise Exception(
            f"Unable to obtain authentication information from Cognito. Response:\n{response}"
        )

    def authorization(self):
        if self.access_token is None:
            self.get_token_()
        return {
            # Execute scripts/get_local_token.cmd before this Python script
            # to get an authorization token. Otherwise the API refuses to
            # accept the connection
            "Authorization": self.access_token
        }

    def get(self, function, waittime=1, **kwdargs):
        body = super().get(function, **kwdargs)
        if body.get("completed", False):
            return body
        key = {"user": body["user"], "id": body["id"]}
        while waittime < 15 * 60:
            if self.debug:
                print(f"Waiting for {waittime}s for '{function}' to complete")
            time.sleep(waittime)
            body = self.get("get", json=key)
            if "Item" in body and body.get("found", False):
                if self.debug:
                    print(f"Found body:\n{body}")
                return json.loads(body["Item"]["computation"])
            waittime *= 2
        raise Exception(f"Unable to complete computation with method '{function}'")

    def post(self, function, waittime=1, **kwdargs):
        body = super().post(function, **kwdargs)
        if body.get("completed", False):
            return body
        key = {"user": body["user"], "id": body["id"]}
        while waittime < 15 * 60:
            if self.debug:
                print(f"Waiting for {waittime}s for '{function}' to complete")
            time.sleep(waittime)
            body = self.post("get", json=key)
            if "Item" in body and body.get("found", False):
                if self.debug:
                    print(f"Found body:\n{body}")
                return json.loads(body["Item"]["computation"])
            waittime *= 2
        raise Exception(f"Unable to complete computation with method '{function}'")


def aws_credentials(username=None, password=None, base_url=None):
    return iQAWSAPI(username=username, password=password, base_url=base_url)
