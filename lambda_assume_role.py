import json
import boto3


def lambda_handler(event, context):
    #client = boto3.client('sts')
    print("Received event: " + json.dumps(event, indent=2))

    # print(event["requestContext"]["authentication"]["clientCert"]["clientCertPem"].encode())
    #raise Exception('Something went wrong')
    #response = client.assume_role(RoleArn=event['rolearn'], RoleSessionName=event['appuuid'], TransitiveTagKeys=['TenantId'], Tags=[{'Key': 'TenantId', 'Value': event['tenantid']}])
    return assume_role_in_customer_account(role=event['rolearn'], tenant=event['orgid'])


def assume_role_in_customer_account(role, tenant):
    client = boto3.client('sts')
    response = client.assume_role(RoleArn=role, RoleSessionName=tenant, TransitiveTagKeys=[
                                  'OrgId'], Tags=[{'Key': 'OrgId', 'Value': tenant}])
    return json.loads(json.dumps(response, default=str))
