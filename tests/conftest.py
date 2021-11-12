import io
import zipfile


def get_test_zip_file():
    pfunc = '''
            def lambda_handler(event, context):
                return event
            '''
    zip_output = io.BytesIO()
    zip_file = zipfile.ZipFile(zip_output, 'w', zipfile.ZIP_DEFLATED)
    zip_file.writestr('lambda_function.py', pfunc)
    zip_file.close()
    zip_output.seek(0)
    return zip_output.read()