import oss

s3 = oss.resource('s3', endpoint_url='https://gateway.99265.net',
                  access_key_id='jxe2ayxct2zrypz2ghrk7ws74ofq',
                  secret_access_key='j2mpch2wa3upgkgshcmdal5fyncdikdouwemk4tjrnsvjrsnduh5e',
                  )
bucket = 'buc1'
key = 'b.exe'
obj = s3.Object(bucket, key)
multipartUpload = obj.initiate_multipart_upload(
    Bucket=bucket,
    Key=key,
)
print(multipartUpload.id)
