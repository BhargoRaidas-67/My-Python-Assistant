name = input("tumhara naam kya hai bhai?").strip().lower()
category = input("category select karo  " \
"joke " \
"tumhara age analysis batau (adult ya student)" \
"Favorite subject ke hisab se suggestion de (match-case use karke)" \
"exit(leave)")
match category:
    case joke if category == joke:
        print("life badi asaan hai na agar bugs fix ho jaate?")
    case analysis if category ==  analysis:
        print("ok")
        age = int(input("tumhara age?"))
        
        if age >= 18:
            print("tum abhi adult ho")
        else:
            print("tm abhi student ho kyoki tum abhi adult nahi ho")
        print("Aur tumhara naam hai" + name)
    case suggestion if category == suggestion:
        subject = input("your faivorite subject?").strip().lower()

        if subject == "maths":
            print("acha scope hai")
        elif subject == "science":
            print("good scope, better future")
        else:
            print("dusre  subject me bhi dhyan do")
    case exit if category == exit:
            print("bye")
            
