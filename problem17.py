digits = ["", "one", "two", "three", "four",
          "five", "six", "seven", "eight", "nine"]
digits_len = map(len, digits)

ten_to_twenty = ["ten", "eleven", "twelve", "thirteen", "fourteen",
                 "sixteen", "seventeen", "eighteen", "nineteen"]
ten_to_twenty_len = map(len, ten_to_twenty)

twenty_to_100 = ["twenty", "thirty", "fourty",
                 "fifty", "sixty", "seventy", "eighty", "ninety"]

twenty_to_100_len = map(len, twenty_to_100)

first_twenty = sum([sum(digits_len), sum(ten_to_twenty_len)])
twenty_to_100_sum = sum(i + j for i in twenty_to_100_len for j in digits_len)
first_99 = first_twenty + twenty_to_100_sum
and_len = len("and")
hundred_len = len("hundred")

reduce(sum, ten_to_twenty_len)
#not solved. got tired of writing stupid code.
