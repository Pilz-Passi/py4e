def combat(health, damage):
    health = health - damage
    if health < 0:
        return 0
    return health

result = combat(20, 30)
print(result)