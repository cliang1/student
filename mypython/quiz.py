import getpass, sys, os

def question_with_response(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg

questions = 7
correct = 0

print('Hello, ' + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(questions) + " questions.")
question_with_response("Are you ready to take a test?")

rsp = question_with_response("Which command allows people to important commands and funcitons?")
if rsp == "import":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("What command defines a funciton")
if rsp == "def":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("What does the print command output?")
if rsp == "the parameter to the terminal":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")
    
rsp = question_with_response("In Jupyter Notebook, what is found below the code cell?")
if rsp == "Output":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")
  

print(getpass.getuser() + " you scored " + str(correct) +"/" + str(questions))