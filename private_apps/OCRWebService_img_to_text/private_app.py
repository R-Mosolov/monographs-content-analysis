from zeep import Client

# Username and license code
LOGIN = 'RM134'
LICENSE = '2C556A14-C5CC-4DE9-A1B5-018C276C98B1'

# Service URL
client = Client('http://www.ocrwebservice.com/services/OCRWebService.asmx?WSDL')

FilePath = "img/efroimson-geniusgenetic-p10-part.png"
with open(FilePath, 'rb') as image_file:
    image_data = image_file.read()

InputImage = {
    'fileName': 'efroimson-geniusgenetic-p10-part.png',
    'fileData': image_data,
}

# Specify coordinates for zones (only from these zone text will be extracted)
# To extract text from all page you do not need setup any zones
ocrZones = {'OCRWSZone': [{'Top': 0, 'Left': 0, 'Height': 900, 'Width': 1600, 'ZoneType': 0},
                          {'Top': 500, 'Left': 1000, 'Height': 150, 'Width': 400, 'ZoneType': 0}]}

OCRSettings = {
    'ocrLanguages': 'RUSSIAN',
    'outputDocumentFormat': 'DOC',
    'convertToBW': 'true',
    'getOCRText': 'true',
    'createOutputDocument': 'true',
    'multiPageDoc': 'true',
    'pageNumbers': 'allpages',
    'ocrZones': ocrZones,
    'ocrWords': 'false',
    'Reserved': '',

}

# Perform OCR recognition
result = client.service.OCRWebServiceRecognize(user_name=LOGIN, license_code=LICENSE, OCRWSInputImage=InputImage,
                                               OCRWSSetting=OCRSettings)

if result.errorMessage:
    # Error occurs during recognition
    print("Recognition Error: " + result.errorMessage)
    exit()

# Available pages 
print("AvailablePages:" + str(result.availablePages))

# Processed pages 
print("Processed Pages:" + str(result.processedPages))

# For zonal or multipage OCR: OCRText[z][p]    z - zone, p - pages

# Extracted text from the first or single page
print("Extracted Text:" + result.ocrText.ArrayOfString[0].string[0])

# Extracted text from the second page (if multipage doc converted)
# print("Extracted Text:" + result.ocrText.ArrayOfString[0].string[1])

# Extracted text from all pages
# for i in range(0, len(result.ocrText.ArrayOfString[0].string)):
#    print("Extracted Text:" + result.ocrText.ArrayOfString[0].string[i])

# Get extracted text from the first zone for each page
# print("Zone 1 Page 1 Text:" + result.ocrText.ArrayOfString[0].string[0])
# print("Zone 1 Page 2 Text:" + result.ocrText.ArrayOfString[0].string[1])

# Get extracted text from the second zone for each page
# print("Zone 2 Page 1 Text:" + result.ocrText.ArrayOfString[1].string[0])
# print("Zone 2 Page 2 Text:" + result.ocrText.ArrayOfString[1].string[1])

# Download output file (if outputformat was specified)
# with open("outputDoc.doc", 'wb') as output_file:
#     file.write(result.fileData)
