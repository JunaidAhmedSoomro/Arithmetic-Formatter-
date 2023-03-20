def arithmetic_arranger(problems, solution = False):

    #Check if number of problems > 5
    if len(problems) > 5:
      return "Error: Too many problems."

    first_operand = []
    second_operand = []
    operator = []
    third_line = []
    fourth_line = []
    #---------------------------------------------------------------------------------------------------------------
    #Split problems into lines
    for problem in problems:

        #Following command is  used to split a string into a list of substrings based on a delimiter () white space.
        symbols = problem.split()
        # symbols = ['32', '+', '698']

        first_operand.append(symbols[0])
        # firs_operand [0] = 32

        operator.append(symbols[1])
        # operator [1] = +
        second_operand.append(symbols[2])
        # second_operand [2] = 698
    # the for loop ended here
    #__________________________________________________________________________________________________________

 #   print(operator)

    # checking if operator is not + or -
    for q in operator:
        if q != '+' and q!= '-':
            return "Error: Operator must be '+' or '-'."

    #Checking if  problems are digits or not
    for i in range(len(first_operand)):
      if not (first_operand[i].isdigit() and second_operand[i].isdigit()):
          # in above line .isdigit() function checks wether or not the string has digits only.
        return "Error: Numbers must only contain digits."
        
    #Check number lenght if its more than 4, we can not entertain it.
    for i in range(len(first_operand)):
        if len(first_operand[i]) > 4 or len(second_operand[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    #Generate dashes
    longest_number = []
    for i in range(len(first_operand)):
        # in follwoing each iteration, retrieving max length of operand to generate dashes accordingly.
        longest_number.append(max(len(first_operand[i]), len(second_operand[i])))
        #print(max(len(first_operand[i]), len(second_operand[i])))

    for i in range(len(longest_number)):
        third_line.append("-"*(longest_number[i]+2)) #+2 ( one for space and one for operator)
        
        
    first_line = []
    for i in range(len(first_operand)):
        if len(first_operand[i]) > len(second_operand[i]):
            first_line.append("  " + first_operand[i])
        else:
            first_line.append(" "*(len(second_operand[i]) - len(first_operand[i]) + 2) + first_operand[i])
                                    #          3-2 +2 = 3 three is multiplied with "  ", and 32 is appended
            # print(first_line) ['   32'] first iteration output.
    
    second_line = []
    for i in range(len(second_operand)):
        if len(second_operand[i]) > len(first_operand[i]):
            second_line.append(operator[i] + " " + second_operand[i])
        else:
            second_line.append(operator[i] + " "*(len(first_operand[i]) - len(second_operand[i]) +1 ) + second_operand[i])

    #Generate solution
    if solution == True:
        for i in range(len(first_operand)):
            if operator[i] == "+":
                a = str(int(first_operand[i]) + int(second_operand[i]))
            else:
                a = str(int(first_operand[i]) - int(second_operand[i]))
            
            if len(a) > max(len(first_operand[i]), len(second_operand[i])):
                fourth_line.append(" " + a)
            else:
                fourth_line.append(" "*(max(len(first_operand[i]), len(second_operand[i])) - len(a) +2 ) + a)
        # print(first_line)
        # print(second_line)
        # print(third_line)
        # print(fourth_line)
        arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line) + "\n" + "    ".join(fourth_line)
    else:
        arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line)

    return arranged_problems