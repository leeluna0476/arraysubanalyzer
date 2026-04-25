# qualtype -> obj by obj. not class by class.
# -> independent function
def filter_by_qualtype(iobj, qtype):
    return [o for o in iobj if qtype == o.qualtype]
