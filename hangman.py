def hangman(word):
    wrong=0
    stages=["",
            "______       ",
            "|     |       ",
            "|     |       ",
            "|     O       ",
            "|    /|>       ",
            "|    / <       ",
            "|            ",
            "|            ",
            ]
    rletters = list(word)
    board =["_"]*len(word)
    win = False
    print("ハングマンへようこそ！")
    
