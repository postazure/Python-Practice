import easygui
#flavor = easygui.buttonbox("What is your favorite flavor of ice cream?", title = "Choose or Die!", choices =["Vanilla", "Chocolate", "Rum Rasin"])
flavor = easygui.enterbox("What is your favorite flavor of ice cream?", default = "Rage Cream")
easygui.msgbox("You picked " + flavor)

