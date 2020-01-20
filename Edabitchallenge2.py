def letter_counter(lst, letter):
    return str(lst).count(letter)

print(letter_counter([
  ["D", "E", "Y", "H", "A", "D"],
  ["C", "B", "Z", "Y", "J", "K"],
  ["D", "B", "C", "A", "M", "N"],
  ["F", "G", "D", "R", "S", "R"],
  ["V", "X", "H", "A", "S", "S"]
], "D"))