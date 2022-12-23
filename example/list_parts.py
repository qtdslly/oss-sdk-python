import oss

s3 = oss.resource('s3', endpoint_url='https://gateway.99265.net',
                  access_key_id='jxe2ayxct2zrypz2ghrk7ws74ofq',
                  secret_access_key='j2mpch2wa3upgkgshcmdal5fyncdikdouwemk4tjrnsvjrsnduh5e',
                  )
bucket = 'buc1'
key = 'b.exe'
uploadId = '7kWxT39UKobQDVmyyNm4NquPvaUksiMPdYyxRtuDg2hDxVD91jdgTYb9octkEdPGFp7EgZbseUe87QGWw9qp3frZ8DFd19mxx8zmJJEjENX6FCXYY96RqJNFEGTjd6UiBWL5DyUNgaUBPwfpno1QWmvSMz4bGzzDiNSdB87F17BYA1xGSuzetJXUkZvuC'

multipart_upload = s3.MultipartUpload(bucket_name=bucket, object_key=key, id=uploadId)
print(multipart_upload.parts.all())
for multipartUploadPart in multipart_upload.parts.all():
    print(multipartUploadPart)
