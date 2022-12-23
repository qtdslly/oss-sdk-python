import oss

s3 = oss.resource('s3', endpoint_url='https://gateway.99265.net',
                  access_key_id='jxe2ayxct2zrypz2ghrk7ws74ofq',
                  secret_access_key='j2mpch2wa3upgkgshcmdal5fyncdikdouwemk4tjrnsvjrsnduh5e',
                  )
bucket = 'buc2'
key = 'a.txt'
obj = s3.Object(bucket, key)
print(obj.bucket_name)
