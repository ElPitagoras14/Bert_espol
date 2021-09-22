from os import getcwd
import contexto
import main

def p_1():
    context_type="Estructura organizacional"
    

    if context_type=="Estructura organizacional":
        context=contexto.context("resources/context_eo.txt")

    elif context_type=="Histórico":
        context=contexto.context("resources/context_h.txt")

    question= "¿Qué es FIEC?"
    result = main.question_answering(question=question, context=context)
    ans="Answer:", result['answer']
    score="Score:", result['score']
    return ans, score

print(p_1())
