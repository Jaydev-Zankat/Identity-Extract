import boto3
from trp import Document

# S3 Bucket Data
s3BucketName = "kshatra-ai-jaydev"

file_path = "/home/ubuntu/kshatra/OCR/id_card/id_card_imgs/Spain1.jpg"

list = file_path.split('/')
file_name = list[-1]

s3 = boto3.client('s3')
s3.upload_file(file_path ,s3BucketName, file_name)

print(".....DONE -UPLOADING.......")


FormdocumentName = file_name
PlaindocumentName = file_name
# TabledocumentName = file_name
# Amazon Textract client
textractmodule = boto3.client('textract')

#1. PLAINTEXT detection from documents:
response = textractmodule.detect_document_text(
    Document={
        'S3Object': {
            'Bucket': s3BucketName,
            'Name': PlaindocumentName
        }
    })
print ('------------- Print Plaintext detected text ------------------------------')
for item in response["Blocks"]:
    if item["BlockType"] == "LINE":
        print ('\033[92m'+str(item['Text'])+'\033[92m')
        x1 = item['Geometry']['BoundingBox']['Left']
        y1 = item['Geometry']['BoundingBox']['Top']
        w = item['Geometry']['BoundingBox']['Width']
        h = item['Geometry']['BoundingBox']['Height']
        #print((x1,y1),(x1+w,y1+h))

# #2. FORM detection from documents:
response = textractmodule.analyze_document(
    Document={
        'S3Object': {
            'Bucket': s3BucketName,
            'Name': FormdocumentName
        }
    },
    FeatureTypes=["FORMS"])
doc = Document(response)

print ('------------- Print Form detected text ------------------------------')
for page in doc.pages:
    for field in page.form.fields:
        print("Key: {}, Value: {}".format(field.key, field.value))



#2. TABLE data detection from documents:
# response = textractmodule.analyze_document(
#     Document={
#         'S3Object': {
#             'Bucket': s3BucketName,
#             'Name': TabledocumentName
#         }
#     },
#     FeatureTypes=["TABLES"])
# doc = Document(response)
# print ('------------- Print Table detected text ------------------------------')
# for page in doc.pages:
#     for table in page.tables:
#         for r, row in enumerate(table.rows):``
#             itemName  = ""
#             for c, cell in enumerate(row.cells):
#                 print("Table[{}][{}] = {}".format(r, c, cell.text))
