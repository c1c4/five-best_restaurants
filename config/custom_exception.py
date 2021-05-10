def handle_not_acceptable(msg):
    """
    Return a error of not acceptable, if one or more of the validation in restaurants controller fails

    :param msg: Could by any msg

    :return: a tuple of str and int
    """
    return msg, 406
