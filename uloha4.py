def find_pairs(number_sequence):

  if len(number_sequence) > 2000 or len(number_sequence) < 2:
    return "Chyba: posloupnost je dlouhá nebo prázdná"

  try:
    number_sequence = [int(num) for num in number_sequence]
  except ValueError:
    return "Chyba: hodnota na vstupu není celé číslo"

  sums_dictionary = {}
  for starting_index in range(len(number_sequence)):
    for ending_index in range(starting_index + 1, len(number_sequence)):
      interval_sum = sum(number_sequence[starting_index:ending_index + 1])
      if interval_sum not in sums_dictionary:
        sums_dictionary[interval_sum] = 1
      else:
        sums_dictionary[interval_sum] += 1

  pair_count = 0
  for sum_value in sums_dictionary.values():
    if sum_value > 1:
      pair_count += sum_value * (sum_value - 1) // 2


user_input_sequence = input("Zadejte posloupnost čísel oddělených mezerou ").split()

print(find_pairs(user_input_sequence))

