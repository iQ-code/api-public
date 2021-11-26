from .bare import iQBareAPI
import boto3

class iQSamAPI(iQBareAPI):
    
    def __init__(self, username, password, base_url='http://127.0.0.1:3000/'):
        super(iQSamAPI, self).__init__(base_url)
        self.username = username
        self.password = password
        self.app_id = "7pjemis07hpeq8rvkqs02sstp3"
        self.access_token = None
    
    def get_token_(self):
        client = boto3.client("cognito-idp", region_name="us-east-1")

        # Initiating the Authentication, 
        response = client.initiate_auth(
            ClientId = self.app_id,
            AuthFlow = "USER_PASSWORD_AUTH",
            AuthParameters = {"USERNAME": self.username, "PASSWORD": self.password},
        )
        # Getting the user details.
        if "AuthenticationResult" in response:
            result = response["AuthenticationResult"]
            if "IdToken" in result:
                self.access_token = result["IdToken"]
                return True
        raise Exception(f'Unable to obtain authentication information from Cognito. Response:\n{response}')

    def authorization(self):
        if self.access_token is None:
            self.get_token_()
        return {
            # Execute scripts/get_local_token.cmd before this Python script
            # to get an authorization token. Otherwise the API refuses to
            # accept the connection
            'Authorization': self.access_token
        }

class iQAWSAPI(iQSamAPI):
    
    def __init__(self, username, password):
        aws_url = 'https://k7z1bo1yw9.execute-api.us-east-1.amazonaws.com/Prod'
        super(iQAWSAPI, self).__init__(username, password, aws_url)

    
def aws_credentials(username, password):
    return iQAWSAPI(username, password)

def sam_credentials(username, password, base_url='http://127.0.0.1:3000/'):
    return iQSamAPI(username, password)


