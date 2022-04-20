import requests

def get_aws_creds(role, org, pemfile, keyfile):
    certificate = (pemfile, keyfile)
    dict = {'rolearn': role, 'orgid': org}
    url_endpoint = 'API Gateway Endpoint'
    resp = requests.get(url_endpoint, params=dict, cert=certificate)
    print(resp.json())


getcreds = get_aws_creds(
    'arn:aws:iam::awsaccountid:role/CustomerAccountARole', 'customerA', 'customera_app1.pem', 'customera_app1.key')
