import oss

s3 = oss.resource('s3', endpoint_url='https://gateway.99265.net',
                  access_key_id='jxe2ayxct2zrypz2ghrk7ws74ofq',
                  secret_access_key='j2mpch2wa3upgkgshcmdal5fyncdikdouwemk4tjrnsvjrsnduh5e',
                  )
bucketName = 'buc2'
object_keys = ['a.txt', 'b.txt']
bucket = s3.Bucket(bucketName)
response = bucket.delete_objects(Delete={
    'Objects': [{
        'Key': key
    } for key in object_keys]
})
