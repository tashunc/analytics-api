def create_status(status):
    return {"status": status}


def server_error_status(status, description):
    return {"status": status,
            "description": description}


def server_error_status_with_expected(status, description, expected):
    return {"status": status,
            "description": description,
            "expected": expected
            }
