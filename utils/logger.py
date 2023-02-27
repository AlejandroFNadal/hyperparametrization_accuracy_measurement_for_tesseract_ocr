def printv(text, verbose_required, verbose, log_file):
    if (verbose_required and verbose) or not verbose_required:
        print(text)
        with open(log_file, 'a') as f:
            f.write(text + '\n')
    return