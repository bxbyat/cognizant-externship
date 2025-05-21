def voter_eligibility():
    age = int(input("How old are you? "))  # asking user for input
    if age >= 18:  # checking if age is 18 or above
        print("Congratulations! You are eligible to vote. Go make a difference! "
              ":P")
    else:  # if age is lower than 18
        print("Oops! You’re not eligible yet. :( But hey, only", 18 - age,
              "more years to go!")


voter_eligibility()