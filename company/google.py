# input -> "aaAAFFfbCcgGGddDD"
# output -> "aAFbGdD"


def google(letters):
  stack = []

  for letter in letters:
    if stack and stack[-1].lower() == letter.lower() and stack[-1] != letter:
      stack.pop()
      continue
    stack.append(letter)
  return "".join(stack)


google("abBcCcgGGGtTt")
