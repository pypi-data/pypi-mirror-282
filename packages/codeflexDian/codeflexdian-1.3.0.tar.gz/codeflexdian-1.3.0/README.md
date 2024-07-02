[![MIT License][license-shield]](https://s3.amazonaws.com/www.codeflex.lat/documentos/c3320017-1937-4353-8881-475e3c89e25e/LICENSE.txt)

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://codeflex.com.co">
    <img src="https://s3.amazonaws.com/www.codeflex.lat/documentos/c3320017-1937-4353-8881-475e3c89e25e/Paginas/logo2.png" alt="Logo" width="260">
  </a>

  <h3 align="center">CODEFLEX CLOUD S.A.S</h3>

  <p align="center">
    Firmar Petición SOAP a la DIAN | NIT: 901829324-9
    <br />
    <a href="https://docs.codeflex.com.co/"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</p>

<!-- ABOUT THE PROJECT -->
## About The Project
 
[![miniatura][miniatura]](https://codeflex.com.co)


<!-- GETTING STARTED 
## Getting Started

### Prerequisites

You need to make sure you have installed the following modules.
* Requests
  ```s
  pip install requests
  ```
-->

### Installation

```python
pip install codeflexDian
```

<!-- USAGE EXAMPLES -->
## Usage

* Example 1 | Lambda Function (AWS) | GetNumberingRange
    ```python 
  import lxml.etree as ET
  from codeflexDian.SOAPSing import SOAPSing
  from codeflexDian.Signing import Signing
  import boto3
  import os
  from string import Template

  def lambda_handler(event, context):
  
      # VARIABLES
      ProviderSub = event['ProviderSub'] # Bucket S3
      accountCode = event['accountCode'] # Código de cuenta del proveedor
      accountCodeT = event['accountCodeT'] # Código de cuenta del proveedor para el conjunto de pruebas
      softwareCode = event['softwareCode'] # Código del software del proveedor
      ProviderEmail = event['ProviderEmail'] # Correo electrónico

      s3subir = boto3.client('s3')
      s3 = boto3.resource('s3')
  
      pathCert = "/tmp/" + ProviderSub + "/certificado.pfx"
      pathClave = "/tmp/" + ProviderSub + "/clave.txt"
      
      metodo = "GetNumberingRange"

      # CREA DIRECTORIO DE TRABAJO SI NO EXISTE
      directory = "/tmp/" + ProviderSub
      if not os.path.exists(directory):
          os.makedirs(directory)
      
      # Descarga el certificado
      s3.Bucket(ProviderSub).download_file("certificado.pfx", pathCert)
      
      # Descarga la clave
      s3.Bucket(ProviderSub).download_file("clave.txt", pathClave)
      
      # Lee la clave
      with open(pathClave) as f:
          passwordCert = f.readline().strip()

      # Si la clave es NA entonces la clave será un blanco
      if (passwordCert == "NA"):
          passwordCert = ""
      
      signing = Signing(pathCert, passwordCert)
      signer = SOAPSing(signing, metodo)
      template = Template('''<wcf:GetNumberingRange xmlns:wcf="http://wcf.dian.colombia"><wcf:accountCode>${accountCode}</wcf:accountCode><wcf:accountCodeT>${accountCodeT}</wcf:accountCodeT><wcf:softwareCode>${softwareCode}</wcf:softwareCode></wcf:GetNumberingRange>''')      
      value = {
          'accountCode': accountCode,
          'accountCodeT': accountCodeT,
          'softwareCode': softwareCode
      }
      templateOk = template.substitute(value)
      element = ET.fromstring(templateOk)
      soapSigned = signer.sing(element)
      soapSingedStrin = ET.tostring(soapSigned)

      # Escribe Request firmado en /tmp
      open('/tmp/' + ProviderSub + '/' + 'RANGOS-SIGN.xml', 'wb').write(soapSingedStrin)
      
      # Sube Request firmado de /tmp a s3
      s3subir.upload_file('/tmp/' + ProviderSub + '/' + 'RANGOS-SIGN.xml', ProviderSub, 'RANGOS-SIGN.xml')
      
      # Retorno de información de destino
      return {
          'ProviderSub': ProviderSub,
          'ProviderEmail': ProviderEmail
      }

    ```

* Example 2 | Lambda Function (AWS) | SendBillSync
    ```python 
  import lxml.etree as ET
  from codeflexDian.SOAPSing import SOAPSing
  from codeflexDian.Signing import Signing
  import base64
  import boto3
  import os
  import json
  from string import Template

  def lambda_handler(event, context):

      """
      Antes de ejecutar este código, asegúrate de zippear la factura XML firmada.
      El código del ejemplo: Example 1 | Lambda Function (AWS) | GetNumberingRange solo 
      se utiliza para consultar los rangos de numeración.
      """
      # Para saber cómo zippear la factura XML firmada con el formato deseado, 
      # consulta el código que está abajo como 'zipfile'.

      #---------------------------------------------------------------------------------------#
  
      # VARIABLES
      ProviderSub = event['ProviderSub'] # Bucket S3
      ProviderEmail = event['ProviderEmail'] # Correo electrónico
      Invoice = event['Invoice'] # Número de la factura EJ: B77404
      IssueDate = event['IssueDate'] # Fecha de emisión de la factura
      TestSetId = event['TestSetId'] # ID del conjunto de pruebas
      Ambiente = event['Ambiente'] # Ambiente de la solicitud (1 para pruebas, 2 para producción)
      
      if Ambiente == "2":
          metodo = "SendTestSetAsync"
      
      if Ambiente == "1":
          metodo = "SendBillSync"

      s3subir = boto3.client('s3')
      s3 = boto3.resource('s3')

      pathCert = "/tmp/" + ProviderSub + "/certificado.pfx"
      pathClave = "/tmp/" + ProviderSub + "/clave.txt"

      # CREA DIRECTORIO DE TRABAJO SI NO EXISTE
      directory = "/tmp/" + ProviderSub
      if not os.path.exists(directory):
          os.makedirs(directory)

      # Descarga el certificado
      s3.Bucket(ProviderSub).download_file("certificado.pfx", pathCert)

      # Descarga la clave
      s3.Bucket(ProviderSub).download_file("clave.txt", pathClave)

      # Lee la clave
      with open(pathClave) as f:
          passwordCert = f.readline().strip()

      # Si la clave es NA entonces la clave será un blanco
      if passwordCert == "NA":
          passwordCert = "" 

      # Descarga la factura xml firmada
      s3.Bucket(ProviderSub).download_file(Invoice + "-ZIP.zip", "/tmp/" + ProviderSub + "/" + Invoice + "-ZIP.zip")

      with open("/tmp/" + ProviderSub + "/" + Invoice + "-ZIP.zip", "rb") as f:
          bytes = f.read()
          encode_string = base64.b64encode(bytes).decode('ascii')

      signing = Signing(pathCert, passwordCert)
      signer = SOAPSing(signing, metodo)
      template = Template('''<wcf:${metodo} xmlns:wcf="http://wcf.dian.colombia"><wcf:fileName>${fileName}</wcf:fileName><wcf:contentFile>${contentFile}</wcf:contentFile><wcf:testSetId>${TestSetId}</wcf:testSetId></wcf:${metodo}>''')
      value = {
          'fileName': Invoice+'.zip',
          'contentFile': encode_string,
          'TestSetId': TestSetId,
          'metodo': metodo
      }

      templateOk = template.substitute(value)
      element = ET.fromstring(templateOk)
      soapSigned = signer.sing(element)
      soapSignedString = ET.tostring(soapSigned)

      # Escribe Request firmado en /tmp
      open('/tmp/' + ProviderSub + '/' + Invoice + '-REQ-SIGN.xml', 'wb').write(soapSignedString)

      # Sube Request firmado de /tmp a s3
      s3subir.upload_file('/tmp/' + ProviderSub + '/' + Invoice + '-REQ-SIGN.xml', ProviderSub, Invoice+'-REQ-SIGN.xml')

      # Retorno de información de destino
      return {
          'ProviderSub': ProviderSub,
          'ProviderEmail': ProviderEmail,
          'Invoice': Invoice,
          'IssueDate': IssueDate,
          'Ambiente': Ambiente
      }

    ```

* zipfile | Lambda Function (AWS)
    ```python 
  import zipfile
  import zlib
  import boto3
  import botocore
  import base64
  import os
  import json

  try:
      import zlib
      compression = zipfile.ZIP_DEFLATED
  except:
      compression = zipfile.ZIP_STORED

  def lambda_handler(event, context):

      # VARIABLES
      ProviderSub = event['ProviderSub'] # Bucket S3
      Factura = event['Factura'] # Número de la factura EJ: B77404

      # TODO implement
      Invoice = Factura
      bucket_name = ProviderSub
      s3subir = boto3.client('s3')
      s3 = boto3.resource('s3') 
      
      #CREA DIRECTORIO DE TRABAJO SI NO EXISTE
      directory = "/tmp/"+Invoice
      if not os.path.exists(directory):
          os.makedirs(directory)

      # DESCARGA DE S3 LA FACTURA FIRMADA
      s3.Bucket(bucket_name).download_file(Factura + "-SIGN.xml", directory+'/SIGN.xml')
      
      #COMPRIMIR EN /TMP
      zf = zipfile.ZipFile('/tmp/' + Invoice + '/zip.zip', mode='w')
      try:
          zf.write('/tmp/' + Invoice + '/SIGN.xml', arcname='firmado.xml', compress_type=compression)
      finally:
          zf.close()
      
      # Sube el archivo a s3
      s3subir.upload_file('/tmp/' + Invoice + '/zip.zip', bucket_name, Factura + "-ZIP.zip")

      return {
          'statusCode': 200,
          'body': json.dumps(Invoice + ".zip, Subido correctamente a S3.")
      }

    ```

_The company that currently uses our library is: [FacturaDian](https://www.facturadian.com/)_

_Download the list of layers to use in Lambda AWS: [Python](https://cflex.link/UsSehzF)_

_OFFICIAL WEBSITE: [CODEFLEX CLOUD S.A.S.](https://codeflex.com.co/)_

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact
Phone: +57 3008130562 |
E-mail: info@codeflex.com.co

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/avmmodules/AVMWeather.svg?style=for-the-badge
[contributors-url]: https://github.com/avmmodules/AVMWeather/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/avmmodules/AVMWeather.svg?style=for-the-badge
[forks-url]: https://github.com/avmmodules/AVMWeather/network/members
[stars-shield]: https://img.shields.io/github/stars/avmmodules/AVMWeather.svg?style=for-the-badge
[stars-url]: https://github.com/avmmodules/AVMWeather/stargazers
[issues-shield]: https://img.shields.io/github/issues/avmmodules/AVMWeather.svg?style=for-the-badge
[issues-url]: https://github.com/avmmodules/AVMWeather/issues
[license-shield]: https://img.shields.io/github/license/avmmodules/AVMWeather.svg?style=for-the-badge
[license-url]: https://github.com/avmmodules/AVMWeather/blob/main/LICENSE
[miniatura]: https://codeflex.com.co/assets/img/ggg.webp
[miniatura2]: https://s3.amazonaws.com/www.codeflex.lat/documentos/76527625-b9dd-4efe-a987-6374f56e3d22/Pagina-Codeflex/Capturadsd.PNG
