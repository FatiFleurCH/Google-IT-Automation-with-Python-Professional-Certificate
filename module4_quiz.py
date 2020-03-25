#Question 1
def format_address(address_string):
  # Declare variables
  address_parts = []
  house_number = ""
  street_name = ""
  # Separate the address string into parts
  address_parts = address_string.split()

  # Traverse through the address parts
  for part in address_parts:
    # Determine if the address part is the
    if part.isnumeric():
      house_number = part
    # house number or part of the street name
    else:
      if part != address_parts[-1]:
        street_name += "".join(part + " ")
      else:
        street_name += "".join(part + "")

  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {house_number} on street named {street_name}".format(house_number = house_number, street_name=street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

#Question 2
def highlight_word(sentence, word):
	return(" ".join([x.upper() if x.lower().replace('!', '') == word else x for x in sentence.split()]))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

#Question 3
def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  new_list = []
  for ele in list2:
    new_list.append(ele)
  # Followed by the elements of list1 in reverse order
  i = len(list1) - 1
  while i >= 0:
    new_list.append(list1[i])
    i -=1
  return new_list
  
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

#Question 4
def squares(start, end):
	return [x**2 for x in range(start,end+1)]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Question 5
def car_listing(car_prices):
  result = ""
  for car, price in car_prices.items():
    result += "{car} costs {price} dollars".format(car=car,price=price) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

#Question 6
def combine_guests(guests1, guests2):
  combined_guests = {}
  for friend_name, number_guests in Rorys_guests.items():
    combined_guests[friend_name] = number_guests
  for friend_name, number_guests in Taylors_guests.items():
    if not(friend_name in combined_guests):
      combined_guests[friend_name] = number_guests
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  return combined_guests
Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

#Question 7
def count_letters(text):
  result = {}
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  # Go through each letter in the text
  for letter in text:
    # Check if the letter needs to be counted or not
    if letter.lower() in alphabet:
      if letter.lower() in result:
        result[letter.lower()] +=1
      else:
        result[letter.lower()] =1
    # Add or increment the value in the dictionary
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
