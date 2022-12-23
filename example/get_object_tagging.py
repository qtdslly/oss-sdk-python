import oss

client = oss.client('s3', endpoint_url='https://gateway.99265.net',
                    access_key_id='jxe2ayxct2zrypz2ghrk7ws74ofq',
                    secret_access_key='j2mpch2wa3upgkgshcmdal5fyncdikdouwemk4tjrnsvjrsnduh5e',
                    )
bucket = 'buc2'
key = 'a.txt'
response = client.get_object_tagging(
    Bucket=bucket,
    Key=key,
)
print(response)
