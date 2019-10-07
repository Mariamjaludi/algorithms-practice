orders = [
  "a1 9 2 3 1",
  "g1 act car",
  "zo4 4 7",
  "ab1 off key dog",
  "a8 act zoo",
  "a4 act zoo"
]

def sortOrders(orders):
  prime = []
  nonPrime = []
  for order in orders:
    strArr = order.split(" ")
    if strArr[1].isalpha():
      prime.append(order)
    else:
      nonPrime.append(order)
  sortPrime(prime)
  return prime + nonPrime

def sortPrime(prime):
  for i in range(len(prime)):
    array = prime[i].split(" ")
    alpha = " ".join(array[1:])
    alphanum = array[0]
    prime[i] = (alpha, alphanum)
  prime.sort()
  formatPrime(prime)

def formatPrime(prime):
  for i in range(len(prime)):
    string = " ".join(prime[i])
    prime[i] = string


print(sortOrders(orders))
