def solution(before, after):
    before = "".join(sorted(before))
    after = "".join(sorted(after))
    if before==after:
        return 1
    else:
        return 0 