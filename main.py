import sys

expression = input ("Digite uma expressão : ")

def sintaxAnaliser (expression) :

    openParentesis = 0
    closeParentesis = 0
    invalidExpression = 0
    typeOfError = ""
    operators = ["+" , "-" , "*" , "/"]
    validCharacters = ["+" , "-" , "*" , "/" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0" , "(" , ")"]

    # no laço de repetição vamos contar o número de parênteses, pois se a subtração deles não for 0 então temos parenteses sobrando ou faltando.
    # no mesmo laço dentro do try tentamos verificar se não há uma expressão com dois operadores seguidos como ++ -+ +*
    for i in range (len (expression)) : 
        if expression [i] == "(":
            openParentesis = openParentesis + 1
        elif expression [i] == ")":
            closeParentesis = closeParentesis + 1

        # identificaremos se há qualquer caractere inválido na expressão
        if expression [i] not in validCharacters : 
            invalidExpression = 1
            typeOfError = "Caractere inválido encontrado. A expressão deve conter apenas números, operadores matemáticos e parênteses. Verifique se não há letras ou espaços em branco na expressão."

        try:
        
            if expression [i] in operators and expression [i+1] in operators:
                invalidExpression = 1
                typeOfError = "Erro na escrita da operação " + expression [i] + expression [i + 1]
        except:

            continue
    
    # verificaremos se não há um operador sobrando no final da expressão
    if expression [len (expression) - 1] in operators:
        invalidExpression = 1
        typeOfError = "Operador " + expression [len (expression) - 1] + " sobrando no último caractere da expressão"

    # verificaremos se não há parênteses sobrando ou falntando
    if openParentesis - closeParentesis < 0:
        invalidExpression = 1
        typeOfError = "Parênteses sobrando"
    elif openParentesis - closeParentesis > 0:
        invalidExpression = 1
        typeOfError = "Parênteses faltando"
    
    if invalidExpression:
        print ("Expressão inválida." + typeOfError)
        sys.exit ()

def toPostFix (expression) :
    stack = []
    postFixExpression = ""
    numbers = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0"]
    operators = ["+" , "-" , "*" , "/" , "("]

    for i in range (len (expression)) : 
        
        # se achar um número já concatena ele na string de saída
        if expression [i] in numbers : 
            postFixExpression = postFixExpression + expression [i]
            print (expression [i] + " adicionado na expressão")

        # se achar um + ou - quem tem menor precedência é apenas o (, então desempilha até chegar nele e depois empilha o + ou -
        if expression [i] == "+" or  expression [i] == "-" :
            while stack and stack [-1] != "(":
                character = stack.pop ()
                postFixExpression = postFixExpression + character
                print ("desempilhou " + character  + " e o adicionou na expressão")
            stack.append (expression [i])
            print (expression [i] + " adicionado na pilha")

        # se achar um * ou /, ninguém tem maior precedência então eles só podem desempilhar operadores iguais a si até poderem se empilhar
        if expression [i] == "*" or  expression [i] == "/" :
            while stack and (stack [-1] == "*" or stack [-1] == "/"):
                character = stack.pop ()
                postFixExpression = postFixExpression + character
                print ("desempilhou " + character + " e o adicionou na expressão")
            stack.append (expression [i])
            print (expression [i] + " adicionado na pilha")

        # se achar um parêntese aberto empilha ele
        if expression [i] == "(" : 
            stack.append (expression [i])
            print (expression [i] + " adicionado na pilha")

        # se achar um parêntese fechado desempilha todo mundo até achar um parêntese aberto, depois empilha o parêntese aberto
        if expression [i] == ")" :
            while stack [-1] != "(":
                character = stack.pop ()
                postFixExpression = postFixExpression + character
                print ("desempilhou " + character + " e o adicionou na expressão")
            print (stack.pop () + " removido da pilha")
        
        #print (stack)

    # se sobrou algúem na pilha desempilha até ela esta vazia e concatena todos na expressão pós fixa
    while stack :
        character = stack.pop ()
        postFixExpression = postFixExpression + character

        if character != "(" :
            print ("desempilhou " + character + " e o adicionou na expressão")
        
        

    print (stack)

    print (postFixExpression)

    return postFixExpression

def calc (expression) : 

    numbers = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0"]
    operands = []
    operators = ["+" , "-" , "*" , "/" , "("]

    for i in range (len (expression)) : 

        #se o caractere atual for um operando (número) converte ele para inteiro e adiciona-o na pilha de operandos
        if expression [i] in numbers:
            operands.append (int (expression [i]))
            print (expression [i] + " empilhado")

        if expression [i] in operators:
            firstOperand = operands.pop ()
            secondOperand = operands.pop ()

            #se o operador encontrado for +, desempilha 2 números e soma o segundo a ser desempilhado com o primeiro
            if expression [i] == "+" : 
                result = secondOperand + firstOperand
                print ("Operando " + str (secondOperand) + " e " + str (firstOperand) + " desempilhados")
                print (str (secondOperand) + "+" + str (firstOperand) + "=" + str (result))
                print ("Empilhando " + str (result))
                operands.append (result)
            
            #se o operador encontrado for -, desempilha 2 números e soma o segundo a ser desempilhado com o primeiro
            if expression [i] == "-" : 
                result = secondOperand - firstOperand
                print ("Operando " + str (secondOperand) + " e " + str (firstOperand) + " desempilhados")
                print (str (secondOperand) + "-" + str (firstOperand) + "=" + str (result))
                print ("Empilhando " + str (result))
                operands.append (result)

            #se o operador encontrado for *, desempilha 2 números e soma o segundo a ser desempilhado com o primeiro
            if expression [i] == "*" : 
                result = secondOperand * firstOperand
                print ("Operando " + str (secondOperand) + " e " + str (firstOperand) + " desempilhados")
                print (str (secondOperand) + "*" + str (firstOperand) + "=" + str (result))
                print ("Empilhando " + str (result))
                operands.append (result)

            #se o operador encontrado for /, desempilha 2 números e soma o segundo a ser desempilhado com o primeiro
            if expression [i] == "/" : 
                result = secondOperand / firstOperand
                print ("Operando " + str (secondOperand) + " e " + str (firstOperand) + " desempilhados")
                print (str (secondOperand) + "/" + str (firstOperand) + "=" + str (result))
                print ("Empilhando " + str (result))
                operands.append (result)

    return operands [-1]


sintaxAnaliser (expression)

print ("\n Pilha da transofrmação infixa para posfixa \n")

postFixExpression = toPostFix (expression)

print ("\n Cálculo da expressão pósfixa \n ")

result = calc (postFixExpression)

print ("\n Resultado Final \n " + expression + "(" + postFixExpression + ")" + "=" + str (result))