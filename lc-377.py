def isCustomerWinner(codeList, shoppingCart):
	if not codeList: return 1
	if not shoppingCart: return 0
	i, j = 0, 0
	while i < len(codeList) and j+len(codeList[i]) <= len(shoppingCart):
		match = True
		for k in range(len(codeList[i])):
			if codeList[i][k] != 'anything' and codeList[i][k] != shoppingCart[j+k]:
				match = False
				break
		if match:
			j+=len(codeList[i])
			i+=1
		else:
			j+=1
	return i == len(codeList)
# space: O(1), RTC: O(M*N), where M is number of total words in codes and N is number of number of items in the cart

print(isCustomerWinner([['apple', 'apple'], ['banana', 'anything', 'banana']], ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']))
print(isCustomerWinner([['apple', 'apple'], ['banana', 'anything', 'banana']], ['banana', 'orange', 'banana', 'apple', 'apple']))
print(isCustomerWinner([['apple', 'apple'], ['banana', 'anything', 'banana']], ['apple', 'banana', 'apple', 'banana', 'orange', 'banana']))
print(isCustomerWinner([['apple', 'banana','apple', 'banana', 'coconut']], ['apple', 'banana', 'apple', 'banana', 'apple', 'banana']))
print(isCustomerWinner([['apple', 'orange'], ['orange', 'banana', 'orange']], ['apple', 'orange', 'banana', 'orange', 'orange', 'banana', 'orange', 'grape']))
print(isCustomerWinner([['apple', 'apple'], ['banana', 'anything', 'banana']], ['apple', 'apple', 'banana', 'banana']))
print(isCustomerWinner([['apple', 'apple'], ['apple', 'anything', 'banana']], ['apple', 'apple', 'banana', 'banana']))
print(isCustomerWinner([['apple', 'apple'], ['apple', 'anything', 'banana']], ['apple', 'apple', 'apple', 'apple', 'banana']))
print(isCustomerWinner([['apple', 'apple'], ['apple', 'banana']], ['apple', 'apple', 'apple', 'banana']))
print(isCustomerWinner([["anything", "apple" ], ["banana", "anything", "banana"]], ["orange", "grapes", "apple", "orange", "orange", "banana", "apple", "banana", "banana"]))
print(isCustomerWinner([['anything']], ['apple', 'apple', 'apple', 'banana']))