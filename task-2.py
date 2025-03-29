from random import randint

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    result = []
    if (min >= 1) and (max <= 1000) and (quantity > min and quantity < max):
        while len(result) != quantity:
            char = randint(min, max)
            if char not in result:
                result.append(char) 

    return sorted(result)   

    




lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)