def main():
  frankenstein_book = "books/frankenstein.txt"
  file_contents = get_file_content(frankenstein_book)
  words = get_number_words_of_text(file_contents)
  unique_characters = get_unique_characters(file_contents)
  sorted_list_unique_characters = dict_to_sorted_list(unique_characters)

  print(f"--- Begin report of {frankenstein_book}")
  print(f"---{words} where found in the document")
  
  for character in sorted_list_unique_characters:
     if not character['char'].isalpha():
        continue
     print(f"The {character['char']} character was found {character['num']} times")
  print("---End report---")
  
def sort_on(dict):
   return dict['num']

def dict_to_sorted_list(dict):
  sorted_list = []
  for character in dict:
    sorted_list.append({"char" : character, "num": dict[character]})
  sorted_list.sort(reverse=True,key=sort_on)
  return sorted_list
   
def get_number_words_of_text(text):
  words = text.split()
  return(len(words))

def get_file_content(file):

  with open(file) as frank:
    return frank.read() 
    
def get_unique_characters(text):

  lower_case_text = text.lower()
  unique_characters = {}

  for character in lower_case_text:
    if character in unique_characters:
         unique_characters[character] += 1
    else:
         unique_characters[character] = 1

  return unique_characters

main()


