OK                                   = 0
ERROR                                = 1
INVALID_ARGUMENT                     = 2
INTERNAL_ERROR                       = 3
REQUIRE_LANG                         = 4

REQUIRE_CAPTCHA                      = 5
CAPTCHA_ERROR                        = 6
VALIDATE_CODE_ERROR                  = 7
PROTECT_OPERATE_ERROR                = 8
PROTECT_OPERATE_REQUIRED             = 9

REQUIRE_NUMBER                       = 10
IMAGE_FORMAT_ERROR                   = 11
FILE_FORMAT_ERROR                    = 12
IMAGE_TOO_BIG                        = 13
CANCEL_FAILED                        = 14

EDIT_FAILED                          = 15
ADD_FAILED                           = 16
CAN_NOT_CANCEL                       = 17
STATUS_PASS                          = 18
DELETE_ERROR                         = 19

STATUS_FINISH                        = 20
STATUS_CREATED                       = 21
STATUS_NOT_PASS                      = 22
IP_NOT_ALLOW                         = 23
ACCESS_ID_NOT_EXIST                  = 24
SIGNATURE_ERROR                      = 25
STATUS_PROCESSING                    = 26
TOO_MANY_REQUESTS                    = 27
CAPTCHA_WAS_USED                     = 28
SMS_REQUEST_TOO_MANY                 = 29
CAS_ERROR                            = 30
APP_UPDATE_CONFIG_EXISTS             = 31
APP_VERSION_LESS                     = 32
APP_UPDATE_LOG_REPEAT                = 33
INVALID_APP_CLIENT_VERSION           = 34


MESSAGES = {
    # 0-99     common error
    0: 'OK',
    1: 'Error',
    2: 'Invalid argument',
    3: 'Internal error',
    4: 'The header is missing a accept-language',

    5: 'Captcha is missing',
    6: 'Captcha error',
    7: 'Verification code error',
    8: 'Protect operate error',
    9: 'Protect operate is required.',
    10: 'Number is required.',

    11: 'Only supports upload png/jpg/jpeg/bmp/gif image format.',
    12: 'Only supports upload .xls file format.',
    13: 'Only supports upload 6M.',
    14: 'Cancel failed',
    15: 'Edit failed',

    16: 'Add failed',
    17: 'Can not cancel',
    18: 'Status pass',
    19: 'Delete error',

    20: 'Status finish',
    21: 'Status created',
    22: 'Status not pass',
    23: 'IP not allow',
    24: 'Access id not exist',
    25: 'Signature error',
    26: 'Status processing',
    27: 'Too many requests',
    28: 'Captcha was used',
    29: 'Sms request too many',
    30: 'Cas api error',
    31: 'App update config exists',
    32: 'App version less than current',
    33: 'App update log repeat',
    34: 'Invalid app1 client version',

}