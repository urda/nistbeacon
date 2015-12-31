"""
Copyright 2015 Peter Urda

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

# https://beacon.nist.gov/certificate/beacon.cer
# noinspection SpellCheckingInspection
NIST_CER_FILE = (
    '-----BEGIN CERTIFICATE-----\n'
    'MIIHZTCCBk2gAwIBAgIESTWNPjANBgkqhkiG9w0BAQsFADBtMQswCQYDVQQGEwJV\n'
    'UzEQMA4GA1UEChMHRW50cnVzdDEiMCAGA1UECxMZQ2VydGlmaWNhdGlvbiBBdXRo\n'
    'b3JpdGllczEoMCYGA1UECxMfRW50cnVzdCBNYW5hZ2VkIFNlcnZpY2VzIFNTUCBD\n'
    'QTAeFw0xNDA1MDcxMzQ4MzZaFw0xNzA1MDcxNDE4MzZaMIGtMQswCQYDVQQGEwJV\n'
    'UzEYMBYGA1UEChMPVS5TLiBHb3Zlcm5tZW50MR8wHQYDVQQLExZEZXBhcnRtZW50\n'
    'IG9mIENvbW1lcmNlMTcwNQYDVQQLEy5OYXRpb25hbCBJbnN0aXR1dGUgb2YgU3Rh\n'
    'bmRhcmRzIGFuZCBUZWNobm9sb2d5MRAwDgYDVQQLEwdEZXZpY2VzMRgwFgYDVQQD\n'
    'Ew9iZWFjb24ubmlzdC5nb3YwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIB\n'
    'AQC/m2xcckaSYztt6/6YezaUmqIqY5CLvrfO2esEIJyFg+cv7S7exL3hGYeDCnQL\n'
    'VtUIGViAnO9yCXDC2Kymen+CekU7WEtSB96xz/xGrY3mbwjS46QSOND9xSRMroF9\n'
    'xbgqXxzJ7rL/0RMUkku3uurGb/cxUpzKt6ra7iUnzkk3BBk73kr2OXFyYYbtrN71\n'
    's0B9qKKJZuPQqmA5n80Xc3E2YbaoAW4/gesncFNL7Sdxw9NIA1L4feu/o8xp3FNP\n'
    'pv2e25C0113x+yagvb1W0mw6ISwAKhJ+6G4t4hFejl7RujuiDfORgzIhHMR4CyWt\n'
    'PZFVn2qxZuVooj1+mduLIXhDAgMBAAGjggPKMIIDxjAOBgNVHQ8BAf8EBAMCBsAw\n'
    'FwYDVR0gBBAwDjAMBgpghkgBZQMCAQMHMIIBXgYIKwYBBQUHAQEEggFQMIIBTDCB\n'
    'uAYIKwYBBQUHMAKGgatsZGFwOi8vc3NwZGlyLm1hbmFnZWQuZW50cnVzdC5jb20v\n'
    'b3U9RW50cnVzdCUyME1hbmFnZWQlMjBTZXJ2aWNlcyUyMFNTUCUyMENBLG91PUNl\n'
    'cnRpZmljYXRpb24lMjBBdXRob3JpdGllcyxvPUVudHJ1c3QsYz1VUz9jQUNlcnRp\n'
    'ZmljYXRlO2JpbmFyeSxjcm9zc0NlcnRpZmljYXRlUGFpcjtiaW5hcnkwSwYIKwYB\n'
    'BQUHMAKGP2h0dHA6Ly9zc3B3ZWIubWFuYWdlZC5lbnRydXN0LmNvbS9BSUEvQ2Vy\n'
    'dHNJc3N1ZWRUb0VNU1NTUENBLnA3YzBCBggrBgEFBQcwAYY2aHR0cDovL29jc3Au\n'
    'bWFuYWdlZC5lbnRydXN0LmNvbS9PQ1NQL0VNU1NTUENBUmVzcG9uZGVyMBsGA1Ud\n'
    'CQQUMBIwEAYJKoZIhvZ9B0QdMQMCASIwggGHBgNVHR8EggF+MIIBejCB6qCB56CB\n'
    '5IaBq2xkYXA6Ly9zc3BkaXIubWFuYWdlZC5lbnRydXN0LmNvbS9jbj1XaW5Db21i\n'
    'aW5lZDEsb3U9RW50cnVzdCUyME1hbmFnZWQlMjBTZXJ2aWNlcyUyMFNTUCUyMENB\n'
    'LG91PUNlcnRpZmljYXRpb24lMjBBdXRob3JpdGllcyxvPUVudHJ1c3QsYz1VUz9j\n'
    'ZXJ0aWZpY2F0ZVJldm9jYXRpb25MaXN0O2JpbmFyeYY0aHR0cDovL3NzcHdlYi5t\n'
    'YW5hZ2VkLmVudHJ1c3QuY29tL0NSTHMvRU1TU1NQQ0ExLmNybDCBiqCBh6CBhKSB\n'
    'gTB/MQswCQYDVQQGEwJVUzEQMA4GA1UEChMHRW50cnVzdDEiMCAGA1UECxMZQ2Vy\n'
    'dGlmaWNhdGlvbiBBdXRob3JpdGllczEoMCYGA1UECxMfRW50cnVzdCBNYW5hZ2Vk\n'
    'IFNlcnZpY2VzIFNTUCBDQTEQMA4GA1UEAxMHQ1JMNjY3MzArBgNVHRAEJDAigA8y\n'
    'MDE0MDUwNzEzNDgzNlqBDzIwMTYwNjEyMTgxODM2WjAfBgNVHSMEGDAWgBTTzudb\n'
    'iafNbJHGZzapWHIJ7OI58zAdBgNVHQ4EFgQUGIOcf6r7Z9wk+2/YuG5oTs7Qwk8w\n'
    'CQYDVR0TBAIwADAZBgkqhkiG9n0HQQAEDDAKGwRWOC4xAwIEsDANBgkqhkiG9w0B\n'
    'AQsFAAOCAQEASc+lZBbJWsHB2WnaBr8ZfBqpgS51Eh+wLchgIq7JHhVn+LagkR8C\n'
    'XmvP57a0L/E+MRBqvH2RMqwthEcjXio2WIu/lyKZmg2go9driU6H3s89X8snblDF\n'
    '1B+iL73vhkLVdHXgStMS8AHbm+3BW6yjHens1tVmKSowg1P/bGT3Z4nmamdY9oLm\n'
    '9sCgFccthC1BQqtPv1XsmLshJ9vmBbYMsjKq4PmS0aLA59J01YMSq4U1kzcNS7wI\n'
    '1/YfUrfeV+r+j7LKBgNQTZ80By2cfSalEqCe8oxqViAz6DsfPCBeE57diZNLiJmj\n'
    'a2wWIBquIAXxvD8w2Bue7pZVeUHls5V5dA==\n'
    '-----END CERTIFICATE-----\n'
)

# https://beacon.nist.gov/certificate/beacon.cer
# noinspection SpellCheckingInspection
NIST_RSA_KEY = (
    '-----BEGIN PUBLIC KEY-----\n'
    'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv5tsXHJGkmM7bev+mHs2\n'
    'lJqiKmOQi763ztnrBCCchYPnL+0u3sS94RmHgwp0C1bVCBlYgJzvcglwwtispnp/\n'
    'gnpFO1hLUgfesc/8Rq2N5m8I0uOkEjjQ/cUkTK6BfcW4Kl8cye6y/9ETFJJLt7rq\n'
    'xm/3MVKcyreq2u4lJ85JNwQZO95K9jlxcmGG7aze9bNAfaiiiWbj0KpgOZ/NF3Nx\n'
    'NmG2qAFuP4HrJ3BTS+0nccPTSANS+H3rv6PMadxTT6b9ntuQtNdd8fsmoL29VtJs\n'
    'OiEsACoSfuhuLeIRXo5e0bo7og3zkYMyIRzEeAslrT2RVZ9qsWblaKI9fpnbiyF4\n'
    'QwIDAQAB\n'
    '-----END PUBLIC KEY-----\n'
)
