import transformers
import matplotlib.pyplot as plt
from transformers import pipeline

question_answering = pipeline("question-answering", model="mrm8488/bert-multi-cased-finetuned-xquadv1", tokenizer="mrm8488/bert-multi-cased-finetuned-xquadv1")

def context(archivo):
    contxt = []
    file = open("resources/" + archivo, 'r', encoding="utf-8")
    contxt = file.readlines()[1]
    file.close()
    return contxt

def respuesta(categoria, pregunta = "¿Cuándo se fundó espol?"):
  ctx = context("ctx_" + categoria + ".txt")
  result = question_answering(context=ctx, question=pregunta)
  historial = open("resources/historial.txt", "a", encoding="utf-8")
  answer = result["answer"]
  score = result["score"]
  historial.write("P: " + pregunta + "|")
  historial.write("R: " + answer.capitalize() + "\n")
  historial.close()
  return (answer, score)

def cargarHistorial():
  pregunta = open("resources/historial.txt", "r", encoding="utf-8")
  lineas_p = pregunta.readlines()
  reverso_p = lineas_p[-6:]
  lista = []
  reverso_p.reverse()
  pregunta.close()
  for pre in reverso_p:
    tmp = pre.split("|")
    lista.append(tmp)
  return lista

def frecuentes(categoria):
  archivo = open("resources/frec_" + categoria + ".txt", "r", encoding="utf-8")
  res = archivo.readlines()
  archivo.close()
  return res