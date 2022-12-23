import oss

client = oss.client('s3', endpoint_url='https://gateway.99265.net',
                    access_key_id='jxe2ayxct2zrypz2ghrk7ws74ofq',
                    secret_access_key='j2mpch2wa3upgkgshcmdal5fyncdikdouwemk4tjrnsvjrsnduh5e',
                    )
bucket = 'buc1'
key = 'b.exe'
uploadId = '7kWxT39UKobQDVmyyNm4NquPvaUksiMPdYyxRtuDg2hDxVD91jdgTYb9octkEdPGFp7FBSEVNPUaRuYjmRN6vd4SLw77knMHSukA5FW3aH516CcFdHaBHAddYJ7yDBo4yQtxqbszbrdtttdHPFqa4ac3LeEVieJ4VemEAsL5c2kTaSQqPHV1ZULwLhAdy'
response = client.abort_multipart_upload(
    Bucket=bucket,
    Key=key,
    UploadId=uploadId,
)
print(response)
