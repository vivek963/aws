import boto3

def lambda_handler(event, context):
    # TODO implement
    #string = event["filecontent"]
    #encoded_string = string.encode("utf-8")
    file_name = event["filename"] + ".txt"
    file_name_1 = event["filename1"] + ".txt"
    file_name_2 = event["filename2"] + ".txt"
    file_content = event["filecontent"]
    file_content_1 = event["filecontent1"]
    bucket_name = "s3-lambda3"
    put(bucket_name,file_name,file_name_1,file_name_2,file_content,file_content_1)
    content = get(bucket_name,file_name,file_name_1,file_name_2)
    print(content)
    combine(bucket_name,file_name_2,file_content,file_content_1)
    
def put(bucket_name_1,file_name_1,file_name_2,file_name_3,file_content_1,file_content_2):    
   
    encoded_file_content = file_content_1.encode("utf-8")
    encoded_file_content_1 = file_content_2.encode("utf-8")
    
    #lambda_path = "/tmp/" + file_name
    #s3_path = "" + file_name    
    
    s3 = boto3.resource("s3")
    s3.Bucket(bucket_name_1).put_object(Key=file_name_1, Body=encoded_file_content)
    s3.Bucket(bucket_name_1).put_object(Key=file_name_2, Body=encoded_file_content_1)
    
    
def get(bucket_name,file_name,file_name_1,file_name_2):
    
    s3client = boto3.client('s3',region_name='eu-west-1')
 
#Create a file object using the bucket and object key. 
    fileobj = s3client.get_object(Bucket=bucket_name,Key=file_name)
    
# open the file object and read it into the variable filedata. 
    filedata = fileobj['Body'].read()

# file data will be a binary stream.  We have to decode it 
    contents = filedata.decode('utf-8')

# Once decoded, you can treat the file as plain text if appropriate 
    return contents

def combine(bucket_name,file_name,file_content,file_content_1):
    combine = file_content + file_content_1
    
    encode_combine = combine.encode("utf-8")
    s3 = boto3.resource("s3")
    s3.Bucket(bucket_name).put_object(Key=file_name, Body=encode_combine)
    