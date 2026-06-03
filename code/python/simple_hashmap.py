# ShopSphere's checkout must total a customer's cart
# against the product catalog. With a large catalog and large
# carts, the lookup strategy decides whether checkout feels
# instant or sluggish. Price the cart as efficiently as possible.

# Given
# A catalog of m products, each with an id and a unit price
# A cart of k lines, each an id and a quantity

# Constraints
# 1 <= m <= 100,000
# 1 <= k <= 100,000
# 0 <= price <= 1,000,000
# 1 <= quantity <= 1,000
# Every cart id exists in the catalog

# Input Format
# Line 1: m. Next m lines: id price. Next line: k. Next k lines: id
# quantity.

# Output Format
# Print one line → Cart Total: <sum of price × quantity>

# Complexity Target: O(m + k) time, O(m) space

m = int(input(""))

prod_catalog = {}

for i in range(m):
    x = input().split(" ")
    prod_catalog[x[0]] = int(x[1])

k = int(input(""))

bill = 0

for i in range(k):
    x = input().split(" ")
    bill += prod_catalog[x[0]] * int(x[1])

print(bill)

# Simple implementation with Python dicts which work exactly like hashmaps