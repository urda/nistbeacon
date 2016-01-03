"""
Copyright 2015-2016 Peter Urda

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

NIST_KEY_FREQUENCY = 'frequency'
NIST_KEY_OUTPUT_VALUE = 'outputValue'
NIST_KEY_PREVIOUS_OUTPUT_VALUE = 'previousOutputValue'
NIST_KEY_SEED_VALUE = 'seedValue'
NIST_KEY_SIGNATURE_VALUE = 'signatureValue'
NIST_KEY_STATUS_CODE = 'statusCode'
NIST_KEY_TIMESTAMP = 'timeStamp'
NIST_KEY_VERSION = 'version'

NIST_INIT_RECORD_TIMESTAMP = 1378395540

# noinspection SpellCheckingInspection
NIST_INIT_RECORD = (
    '{'
    '"frequency": 60, '
    '"outputValue": '
    '"17070B49DBF3BA12BEA427CB6651ECF7860FDC3792268031B77711D63A8610F4CDA551B7'
    'FB331103889A62E2CB23C0F85362BBA49B9E0086D1DA0830E4389AB1", '
    '"previousOutputValue": '
    '"000000000000000000000000000000000000000000000000000000000000000000000000'
    '00000000000000000000000000000000000000000000000000000000", '
    '"seedValue": '
    '"87F49DB997D2EED0B4FDD93BAA4CDFCA49095AF98E54B81F2C39B5C4002EC04B8C9E31FA'
    '537E64AC35FA2F038AA80730B054CFCF371AB5584CFB4EFD293280EE", '
    '"signatureValue": '
    '"F93BBE5714944F31983AE8187D5D94F87FFEC2F98185F9EB4FE5DB61A9E5119FB0756E9A'
    'F4B7112DEBF541E9E53D05346B7358C12FA43A8E0D695BFFAF193B1C3FFC4AE7BCF665181'
    '2B6D60190DB8FF23C9364374737F45F1A89F22E1E492B0F373E4DB523274E9D31C86987C6'
    '4A26F507008828A358B0E166A197D433597480895E9298C60D079673879C3C1AEDA6306C3'
    '201991D0A6778B21462BDEBB8D3776CD3D0FA0325AFE99B2D88A7C357E62170320EFB51F9'
    '749B5C7B9E7347178AB051BDD097B226664A2D64AF1557BB31540601849F0BE3AAF31D7A2'
    '5E2B358EEF5A346937ADE34A110722DA8C037F973350B3846DCAB16C9AA125F2027C246FD'
    'B3", '
    '"statusCode": "1", '
    '"timeStamp": 1378395540, '
    '"version": "Version 1.0"'
    '}'
)

NIST_XML_TEMPLATE = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<record xmlns="http://beacon.nist.gov/record/0.1/">'
    '<version>{0}</version>'
    '<frequency>{1}</frequency>'
    '<timeStamp>{2}</timeStamp>'
    '<seedValue>{3}</seedValue>'
    '<previousOutputValue>{4}</previousOutputValue>'
    '<signatureValue>{5}</signatureValue>'
    '<outputValue>{6}</outputValue>'
    '<statusCode>{7}</statusCode>'
    '</record>'
)
