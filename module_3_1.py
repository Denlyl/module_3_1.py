calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    my_typle = (len(string), string.upper(), string.lower())
    return my_typle

def is_contains(string, list_to_search):
    count_calls()
    my_typle2 = string.upper() in [i.upper() for i in list_to_search]
    return my_typle2

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)