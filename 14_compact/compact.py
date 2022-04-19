def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    
    # results = []
    # for val in lst:
    #     if val != None:
    #         results.append(val)
    # print(results)
    
    return [val for val in lst if val]
