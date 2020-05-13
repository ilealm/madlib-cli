from madlib_cli.madlib import read_file, find_nouns


def test_read_file_one():
  # if the return value is truthy, then the the test can pass 
  actual = read_file("assets/script_one.txt")  
  assert actual

def test_read_file_two():
  # read a file with 2 lines
  actual = read_file("assets/short_file.txt")
  expected = "hola\nadios"
  assert actual == expected


def test_find_nouns_one():
  content = "I the {Adjective} and {Noun} {A First Name} have {Past Tense Verb}{A First Name}'s {Adjective}"
  actual = find_nouns(content)
  expected = ['Adjective','Noun','A First Name','Past Tense Verb','A First Name', 'Adjective']
  assert actual == expected