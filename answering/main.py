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
  archivo = open("resources/historial.txt", "a", encoding="utf-8")
  answer = result["answer"]
  score = result["score"]
  archivo.write("R: " + answer.capitalize() + "\n")
  archivo.write("P: " + pregunta.capitalize() + "\n")
  archivo.close()
  return (answer, score)

def cargarHistorial():
  archivo = open("resources/historial.txt", "r", encoding="utf-8")
  lineas = archivo.readlines()
  reverso = lineas[-8:]
  reverso.reverse()
  archivo.close()
  return reverso

def frecuentes(categoria):
  archivo = open("resources/frec_" + categoria + ".txt", "r", encoding="utf-8")
  res = archivo.readlines()
  archivo.close()
  return res