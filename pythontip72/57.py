
def cigar_party(cigars, is_weekend):
    if is_weekend:
        if cigars > 40:
            return True
    if 40 <= cigars <= 60:
        return True
    return False