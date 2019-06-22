import language_check


text='this are bad'
def correct(text, threshold=1000):
    tool = language_check.LanguageTool('en-US')
    i = 0
    matches = tool.check(text)
    while matches or i < threshold:
        matches = tool.check(text)
        text = language_check.correct(text, matches)
        i += 1

    return text
output = correct("this are bad.")
print(output)