# python3 hello_person.py -n "mahesh " -l "Tamil"
# cannot run this file directly in terminal window use above line to run the file so we can get the output for the file


def hello(name,lang):
    greetings ={"English": "Hello","Tamil":"Vanakkam",
            "Hindi":"Namasate"}
    msg = f"{greetings[lang]} {name}"
    print(msg)

if __name__ == '__main__':
    import  argparse

    parser = argparse.ArgumentParser(description = "Provides a person greeting.")

    parser.add_argument( "-n","--name",metavar="name",
                        required=True,help = "The name of the person to greet.") #  condition to argument for pritng name 
    parser.add_argument("-l", "--lang", metavar= "language",
                        required = True, choices= ["English","Tamil","Hindi"],help = "The language of the greeting") # Condition to  argument to print language
    args = parser.parse_args()

    # msg = f"Hello {args.name}!"

    # print(msg)
    hello(args.name,args.lang)

