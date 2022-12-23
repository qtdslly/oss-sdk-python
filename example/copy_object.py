import oss

s3 = oss.resource('s3', endpoint_url='https://gateway.99265.net',
                  access_key_id='jxe2ayxct2zrypz2ghrk7ws74ofq',
                  secret_access_key='j2mpch2wa3upgkgshcmdal5fyncdikdouwemk4tjrnsvjrsnduh5e',
                  )
source_bucket = 'buc2'
source_key = 'a.txt'
destination_bucket = 'buc1'
destination_key = 'c/aab.txt'
destination_object = s3.Object(destination_bucket, destination_key)
destination_object.copy_from(CopySource={
    'Bucket': source_bucket,
    'Key': source_key
})
