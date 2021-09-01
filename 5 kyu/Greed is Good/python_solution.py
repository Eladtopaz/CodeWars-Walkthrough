def score(dice):
    score = 0
    if dice.count(6) >= 3:
        if dice.count(6) == 6:
            return 1200
        score += 600

    if dice.count(4) >= 3:
        if dice.count(4) == 6:
            return 800
        score += 400

    if dice.count(3) >= 3:
        if dice.count(3) == 6:
            return 600
        score += 300

    if dice.count(2) >= 3:
        if dice.count(2) == 6:
            return 400
        score += 200
    
    count_1 = dice.count(1)
    if count_1 >= 3:
        if count_1 == 6:
            return 2000
        score += 1000
        count_1 -= 3
    
    count_5 = dice.count(5)
    if count_5 >= 3:
        if count_5 == 6:
            return 1000
        score += 500
        count_5 -= 3
        
    score += (count_5 * 50) + (count_1 * 100)
    return score
