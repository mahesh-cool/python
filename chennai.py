from random import choice

capital = "chennai"

bird = "peacock"

flower = " lotus"

song = "yar alaipatheu"

def randomfacts():
    funfacts = [
        "Chennai was the first city in India to have a vast network of Wi-Fi. It’s always been ahead of the curve when it comes to technology! ",
        "Automobile Capital: Often referred to as the “Detroit of South Asia,” Chennai is a hub for the automobile industry. It’s home to major car manufacturers and plays a significant role in India’s automotive sector. 🚗",
        "Oldest Prison: Chennai Central prison holds the distinction of being the oldest prison in India",
        "Name Origins: The name “Chennai” has Telugu origins. It was derived from the name of a Telugu ruler, Damarla Mudirasa Chennappa Nayakudu, whose lineage connects to the British acquisition of the town in 1639.",
        "Marina Beach: Chennai boasts the world’s second-largest urban beach, the iconic Marina Beach. It’s a great place to unwind and enjoy the sea breeze",
        "Green Cover: As of 2018, Chennai had a green cover of 14.9%, exceeding the World Health Organization’s recommendation of 9 square meters of green cover per capita in cities",
        "Name Change: In 1996, the Government of Tamil Nadu officially changed the city’s name from Madras to Chennai. Many Indian cities underwent similar name changes during that time.",
        "World War Connection: Chennai is the only Indian city that was attacked during World War I. It has a unique historical significance. "
    ]
    index = choice("01234567")    
    print(funfacts[int(index)])
if __name__ =="__main__":
     randomfacts()
# randomfacts()