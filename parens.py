def gen(n, cur, open, closed):
    if len(cur) == n * 2:
        print(cur)
        return
    if open < n:
        gen(n, cur + "(", open + 1, closed)
    if closed < open:
        gen(n, cur + ")", open, closed + 1)


def parens(n):
    gen(n, "", 0, 0)


parens(2)
# assert parens(1) == "()"
# assert parens(2) == ["()()","(())"]
