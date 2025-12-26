def evaluate(state, result):
    """
    Evaluates the output of the Executor.
    Returns a decision string.
    """

    if state == "CHECK_ELIGIBILITY":
        if not result or len(result) == 0:
            return "NO_SCHEME_FOUND"
        return "SCHEME_FOUND"

    return "OK"
