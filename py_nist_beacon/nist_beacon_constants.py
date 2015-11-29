NIST_KEY_FREQUENCY = 'frequency'
NIST_KEY_OUTPUT_VALUE = 'outputValue'
NIST_KEY_PREVIOUS_OUTPUT_VALUE = 'previousOutputValue'
NIST_KEY_SEED_VALUE = 'seedValue'
NIST_KEY_SIGNATURE_VALUE = 'signatureValue'
NIST_KEY_STATUS_CODE = 'statusCode'
NIST_KEY_TIMESTAMP = 'timeStamp'
NIST_KEY_VERSION = 'version'

NIST_XML_TEMPLATE = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<record>'
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
