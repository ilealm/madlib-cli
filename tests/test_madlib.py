from madlib_cli.madlib import read_file


def test_read_file_one():
  # if the return value is truthy, then the the test can pass 
  actual = read_file("assets/script_one.txt")  
  assert actual

def test_read_file_two():
  # read a file with 2 lines
  actual = read_file("assets/short_file.txt")
  expected = "hola\nadios"
  assert actual == expected
