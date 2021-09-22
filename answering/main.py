import transformers
import matplotlib.pyplot as plt
from transformers import pipeline
from .contexto import *

question_answering = pipeline("question-answering", model="mrm8488/bert-multi-cased-finetuned-xquadv1", tokenizer="mrm8488/bert-multi-cased-finetuned-xquadv1")


def respuesta(categoria, pregunta = "¿Cuándo se fundó espol?"):
  ctx = context("ctx_" + categoria + ".txt")
  result = question_answering(context=ctx, question=pregunta)
  archivo = open("resources/historial.txt", "a", encoding="utf-8")
  answer = result["answer"]
  score = result["score"]
  archivo.write("R:" + answer.capitalize() + "\n")
  archivo.write("P:" + pregunta.capitalize() + "\n")
  archivo.close()
  return (answer, score)

def cargarHistorial():
  archivo = open("resources/historial.txt", "r", encoding="utf-8")
  lineas = archivo.readlines()
  reverso = lineas[-8:]
  reverso.reverse()
  return reverso