THIRD_PARTY_ERROR = "Third Party Error Please Check Inputs"
INVALID_INPUT = "Enter Valid Inputs"

class ItemAlreadyStored(Exception):
    pass


class WrongParam(Exception):
    pass


class BadRequest(Exception):
    pass


class ThirdPartyError(Exception):
    pass
