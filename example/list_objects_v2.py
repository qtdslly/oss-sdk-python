import oss

client = oss.client('s3', endpoint_url='https://gateway.99265.net',
                  access_key_id='jxe2ayxct2zrypz2ghrk7ws74ofq',
                  secret_access_key='j2mpch2wa3upgkgshcmdal5fyncdikdouwemk4tjrnsvjrsnduh5e',
                  )
bucketName = "buc1"
prefix = '/'
response = client.list_objects_v2(
    Bucket=bucketName,
    Prefix=prefix,
)
print(response)
