"""

words1 = [ "The", "day", "began", "as", "still", "as", "the",
          "night", "abruptly", "lighted", "with", "brilliant",
          "flame" ]

wrapLines(words1, 13) "wrap words1 to line length 13" =>

  [ "The-day-began",
    "as-still-as",
    "the-night",
    "abruptly",
    "lighted-with",
    "brilliant",
    "flame" ]

wrapLines(words1, 20) "wrap words1 to line length 20" =>

  [ "The-day-began-as",
    "still-as-the-night",
    "abruptly-lighted",
    "with-brilliant-flame" ]
    
words2 = [ "Hello" ]


"""

def wrapLines2(words, max_len):
  i, n = 0, len(words)
  line, res = [], []
  while i < n:
    j = i + 1
    line_len = len(words[i])
    line.append(words[i])
    while j < n and (line_len + len(words[j]) + (j-i)-1) < max_len:
      line_len += len(words[j])
      line.append(words[j])
      j += 1
    res.append('-'.join(line))
    line = []
    i = j
  print(res)




def wrapLines(words, max_len):
  i, curr, dashes, line_len, word_count, line, res, rem = 0, '', 0, 0, 0, [], [], ''
  while i < len(words):
    if line_len <= max_len:
      curr += words[i]
      line.append(words[i])
      line_len = len(curr) 
      word_count += 1
      if line_len + word_count - 1 >= max_len:
        if line_len + word_count -1 > max_len:
          i -= 1
          rem = line.pop()
        res.append('-'.join(line))
        curr, dashes, line_len, word_count, line =  '', 0, 0, 0, []
    i += 1

  if rem:
    res.append(rem)

  return res

words1 = [ "The", "day", "began", "as", "still", "as", "the",
          "night", "abruptly", "lighted", "with", "brilliant",
          "flame" ]

print(wrapLines2(words1, 13))



