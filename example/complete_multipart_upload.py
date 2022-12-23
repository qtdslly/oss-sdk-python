import oss

client = oss.client('s3', endpoint_url='https://gateway.99265.net',
                    access_key_id='jxe2ayxct2zrypz2ghrk7ws74ofq',
                    secret_access_key='j2mpch2wa3upgkgshcmdal5fyncdikdouwemk4tjrnsvjrsnduh5e',
                    )
bucket = 'buc1'
key = 'b.exe'
uploadId = '7kWxT39UKobQDVmyyNm4NquPvaUksiMPdYyxRtuDg2hDxVD91jdgTYb9octkEdPGFp7EgZbseUe87QGWw9qp3frZ8DFd19mxx8zmJJEjENX6FCXYY96RqJNFEGTjd6UiBWL5DyUNgaUBPwfpno1QWmvSMz4bGzzDiNSdB87F17BYA1xGSuzetJXUkZvuC'
etag1 = '"a84196d8618498781f7e6d464b928cb0"'
partNumber1 = 1
etag2 = '"93252f429fa8f02078282c9caaeb6ace"'
partNumber2 = 2
response = client.complete_multipart_upload(
    Bucket=bucket,
    Key=key,
    UploadId=uploadId,
    MultipartUpload={
        'Parts': [
            {
                'ETag': etag1,
                'PartNumber': partNumber1
            },
            {
                'ETag': etag2,
                'PartNumber': partNumber2
            },
        ]
    },
)
print(response)
