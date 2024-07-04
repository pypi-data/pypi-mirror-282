"""This contains utils to parse the message."""


def comma_join(fields, oxford=True):
    """Join together words."""

    def fmt(field):
        return "'%s'" % field

    if not fields:
        # unfortunately this happens: we get 'modify' messages with no
        # 'changes', so we don't know what changed
        return "something unknown"
    elif len(fields) == 1:
        return fmt(fields[0])
    elif len(fields) == 2:
        return " and ".join([fmt(f) for f in fields])
    else:
        result = ", ".join([fmt(f) for f in fields[:-1]])
        if oxford:
            result += ","
        result += " and %s" % fmt(fields[-1])
        return result
