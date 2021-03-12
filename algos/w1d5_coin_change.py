# Generate Coin Change
# Change is inevitable (especially when breaking a twenty).

# Make generateCoinChange(cents).
# Accept a number of American cents, compute and print how to represent that amount with smallest number of coins. Common American coins are pennies (1 cent), nickels (5 cents), dimes (10 cents), and quarters (25 cents). Return the optimal configuration of coins in an object.

# Example output, given generateCoinChange(94), return
# { quarters:3, dimes:1, nickels:1, pennies:4}

def generate_coin_change(cents):
    optimal = {
        'quarters': 0,
        'dimes': 0,
        'nickels': 0,
        'pennies': 0
    }

    optimal['quarters'] = int(cents/25)
    cents -= optimal['quarters'] * 25

    optimal['dimes'] = int(cents/10)
    cents -= optimal['dimes'] * 10

    optimal['nickels'] = int(cents/5)
    cents -= optimal['nickels'] * 5

    optimal['pennies'] = cents

    return optimal

print(generate_coin_change(94))