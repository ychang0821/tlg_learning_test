

extension_list = {'Albert': 'ext21', 'Beth': 'ext42', 'Charles': 'ext7'}
extension_list.update({'James':'ext87'})
extension_list.update({'Albert':'ext100'})

print(extension_list)

print(extension_list.keys())    # get the keys of a dictionary

print(extension_list.values())    # get the values of a dictionary

# how to index a dictionary
print(extension_list['Albert'])   #'ext21'
print(extension_list['Beth'])     #'ext42'
print(extension_list['Charles'])  #'ext7'

print(extension_list.get('Albert'))     # gives value, = extension_list['Albert']
extension_list['Beth'] = 'ext55'      # using square brackets allow us to reassign dict values
print(extension_list)

x = [2, 4, 6]
x.append(8)    # [2, 4, 6, 8]
print(x)

y = [1, 3, 5, 9]
y.pop()  # [1, 3, 5]
print(y)

extension_list.popitem()    # removes 'James': 'ext87'
print(extension_list)

extension_list.pop('Albert')  # removes 'Albert': 'ext100'
print(extension_list)

# dictionary example
# keys in dictionary have to be immutable
phone_book = { 'pizza': ['253-374-2832', '253-374-8372', '253-734-2834'],
               'auto': ['253-474-9723', '253-634-2732', '253-632-8621'],
               'restaurant': ['253-3632-8376', '253-253-2532', '253-732-9821']
               }

print(phone_book['pizza'])      # ['253-374-2832', '253-374-8372', '253-734-2834']
print(phone_book['pizza'][1])   # 253-374-8372
print(phone_book)