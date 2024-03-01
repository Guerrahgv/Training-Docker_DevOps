from fastapi import FastAPI, HTTPException

from fastapi.responses import JSONResponse


app=FastAPI()



@app.get("/")
async def index():
    return {
        "titulo": "Mi api con FastAPI utilizando Docker en DevOps",
        "version": "1.0",
        "autor": "Henry Guerrero",
    }

@app.get("/sumar")
async def sumar(num1:int , num2:int):
  try:
    a =num1
    b=num2
    resultado = a + b
    return JSONResponse({"resultado": resultado, "status": 200})
  except ValueError:
    raise HTTPException(status_code=400, detail="Parámetros no válidos")
  

@app.get("/restar")
async def resta(num1:int , num2:int):
  try:
    a =num1
    b=num2
    resultado = a - b
    return JSONResponse({"resultado": resultado, "status": 200})
  except ValueError:
    raise HTTPException(status_code=400, detail="Parámetros no válidos")
  
@app.get("/multiplicar")
async def multiplica(num1:int , num2:int):
  try:
    a =num1
    b=num2
    resultado = a * b
    return JSONResponse({"resultado": resultado, "status": 200})
  except ValueError:
    raise HTTPException(status_code=400, detail="Parámetros no válidos")

@app.get("/dividir")
async def divide(num1:int , num2:int):
  try:
    a =num1
    b=num2
    resultado = a / b
    resultado= float(resultado)
    return JSONResponse({"resultado": resultado, "status": 200})
  except ValueError:
    raise HTTPException(status_code=400, detail="Parámetros no válidos")