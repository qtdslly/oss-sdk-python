import oss

s3 = oss.resource('s3', endpoint_url='https://gateway.99265.net',
                  access_key_id='jxe2ayxct2zrypz2ghrk7ws74ofq',
                  secret_access_key='j2mpch2wa3upgkgshcmdal5fyncdikdouwemk4tjrnsvjrsnduh5e',
                  )
bucket = 'buc1'
key = 'b.exe'
uploadId = '7kWxT39UKobQDVmyyNm4NquPvaUksiMPdYyxRtuDg2hDxVD91jdgTYb9octkEdPGFp7EkjJSJpE3EJnFtgcc8NFfNZf9s9XopXrXws5igM2KUiif1HCAtDcvCioNSaxKbNLSp4ur3T3Gi8LLXyRXFL4f1A43mMNMHHmhM9xcQLAviKY5UfgdGhnSjr9tM'
partNumber = 2
filePath = 'D:\\xab'
try:
    put_data = open(filePath, 'rb')
except IOError:
    raise
try:
    multipart_upload_part = s3.MultipartUploadPart(bucket_name=bucket, object_key=key, multipart_upload_id=uploadId,
                                                   part_number=partNumber)
    response = multipart_upload_part.upload(Body=put_data)
    print(response['ETag'])
finally:
    if getattr(put_data, 'close', None):
        put_data.close()
