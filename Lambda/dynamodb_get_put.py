import boto3
from pprint import pprint
from botocore.exceptions import ClientError

def get_emp(v_emp_id,table):
    
    try:
        response = table.get_item(Key={'emp_id':v_emp_id})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response

def put_emp(emp_id, age, name,table):
    
    
    response = table.put_item(
       Item={
            'emp_id':emp_id,
            'age': age,
            'name':name
        }
    )
    return response


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb',region_name='eu-west-1')
    table = dynamodb.Table('emp_data')
   
    for i in range(4,100):
        emp_id = str(i)
        name = "name" + emp_id
        age = "age" + emp_id
        emp_add = put_emp(emp_id,age,name,table)
   
    emp_record = get_emp(event['emp_id'],table)
    emp_add = put_emp(event['emp_id'],event['age'],event['name'],table)
    pprint(emp_add, sort_dicts=False)
    

    
    