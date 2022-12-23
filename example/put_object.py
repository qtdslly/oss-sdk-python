import oss

s3 = oss.resource('s3', endpoint_url='https://gateway.99265.net',
                  access_key_id='jxe2ayxct2zrypz2ghrk7ws74ofq',
                  secret_access_key='j2mpch2wa3upgkgshcmdal5fyncdikdouwemk4tjrnsvjrsnduh5e',
                  )
bucket = 'buc2'
key = 'a2/a.txt'
filePath = 'D:\\a.txt'
obj = s3.Object(bucket, key)
try:
    put_data = open(filePath, 'rb')
except IOError:
    raise
try:
    obj.put(Body=put_data)
    obj.wait_until_exists()
finally:
    if getattr(put_data, 'close', None):
        put_data.close()
