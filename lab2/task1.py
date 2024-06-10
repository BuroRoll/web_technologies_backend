import boto3



class Storage:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.s3 = boto3.client('s3',
                               endpoint_url='storage.yandexcloud.net',
                               region_name='u-central1-a',
                               aws_access_key_id='YCAJEhWoQ1CM6BsfAlpT4SL3M',
                               aws_secret_access_key='YCMJpHzBM_foD-Qa26G1RjWE47Dj3Mh9CtFFYEF2'
                               )

    def save_file(self, file_name):
        try:
            self.s3.upload_file('f' + file_name, self.bucket_name, file_name)
        except Exception as e:

            raise e

        file_url = f'{self.s3.meta.endpoint_url}/{self.bucket_name}/{file_name}'

        return file_url