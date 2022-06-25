def printv(text, verbose_required, verbose):
    if (verbose_required and verbose) or not verbose_required:
        print(text)
    return