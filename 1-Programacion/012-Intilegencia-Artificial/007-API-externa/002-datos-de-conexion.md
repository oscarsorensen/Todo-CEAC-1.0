Interfaz web para usuario final:
https://chatgpt.com/

Interfaz de programador
https://auth.openai.com/log-in

En API Keys definimos puertas de conexion

Las API Keys son secretas
Deben utilizarse con variables de entorno

O bien mediante archivos .env
O bien mediante archivos JSON
O bien mediante variables de entorno en Linux

En definitiva, la clave nunca debe estar en el código





# What is an API?

API stands for *Application Programming Interface*. An API is a system that allows one program to communicate with another program in a structured and defined way.

An API acts as an intermediary. Instead of a program needing to know how another program works internally, it can send a request to the API and receive a response. The API defines exactly what requests are allowed and what responses will be returned.

## How an API works

The process typically works like this:

1. A program sends a request to the API.
2. The API receives the request and forwards it to the appropriate service.
3. The service processes the request.
4. The API sends a response back to the original program.

This allows different systems to work together without needing direct internal access to each other.

## Example

If a program wants to retrieve information about a property, it can send a request to an API:

