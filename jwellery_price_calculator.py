import time

def jewel_category():
    category = print("PLEASE SELECT CATEGORY OF JWELLERY !!")
    time.sleep(1)
    category_decision = input("PRESS g FOR GOLD (HALLMARK) OR PRESS s FOR SILVER (HALLMARK): ")

    if category_decision == 'g':
        gold_calculation()

    elif category_decision == 's' :
        silver_calculation()

    else:
        print("SORRY YOU HAVE CHOOSE WRONG OPTION FROM THE DESIRE CATEGORY !!!!")


def gold_calculation():
    gold_category = print("YOU HAVE SELECTED CATEGORY OF GOLD")
    time.sleep(1)    
    gold_rate = int(input("ENTER HOW MUCH GOLD RATE PER 10 GRAM IS REQUIRED: "))
    gold_weight = float(input("ENTER WEIGHT OF GOLD IN GRAMS: "))
    labour = int(input("ENTER HOW MUCH LABOUR PER GRAM DO YOU WANT IN RUPPES: "))
    wastage = int(input("ENTER HOW MUCH WASTAGE DO YOU WANT IN PERCENT: "))
    
    gold_price_calculation = ((((( ( gold_weight + (( gold_weight * wastage ) / 100 ))) * (gold_rate) )) / 10 ) + (gold_weight * labour))
    
    print("CALCULATION ON PROGRESS....")
    time.sleep(1)
    
    print(f"JEWELLERY PRICE = {gold_price_calculation}")

def silver_calculation():
    silver_category = print("YOU HAVE SELECTED CATEGORY OF SILVER")
    
    silver_rate = int(input("ENTER HOW MUCH SILVER RATE PER 10 GRAM IS REQUIRED: "))
    silver_weight = float(input("ENTER WEIGHT OF SILVER IN GRAMS: "))    
    labour = int(input("ENTER HOW MUCH LABOUR DO YOU WANT IN RUPPES: "))

    silver_price_calculation = ((( silver_weight * silver_rate) / 10 ) + labour )
    
    print("CALCULATION ON PROGRESS....")
    time.sleep(1)
    
    print(f"SILVER PRICE = {silver_price_calculation}")

def main():
    confirmation = input("TO CALCULATE THE PRICE OF THE JWELLER, PRESS ENTER KEY TO CONTINUE... ")

    if confirmation == "":
        jewel_category()
        
    else:
        print("SORRY YOU HAVE PRESSED THE WRONG KEY, PLEASE PRESS ENTER KEY.")

main()
