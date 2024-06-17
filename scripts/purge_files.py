def entrypoint(parameters: dict = {}):
    try:
        return {
            "status": "ok",
            "data": "ALL FILES DELETED - I hope that's what you wanted",
        }
    except Exception as e:
        return {"status": "exception", "exception": e}


def declaration():
    return {
        "name": "Purge Files",
        "behaviors": {"mutating": True, "dangerous": True, "slow": False},
        "parameters": {},
    }
