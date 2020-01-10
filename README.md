## Como acceder al carrito de Steren
1. Inspect Element -> Application -> Local Storage
2.  En el elemento www.steren.com.mx buscar la key "mage-cache-storage"
3.  En la key "mage-cache-storage" buscar el atributo "cart".
4.  Click derecho al atributo cart y seleccionar store as global variable
5.  Abrir la consola de y debe aparecer una variable "temp#" imprimiendose en la consola.
6.  Ejecutar el comando copy(temp#)
7.  En este punto ya deberia de estar el carrito en el formato json en nuestro clipboard


## Como extraer informacion del carrito de steren a csv.
1. guardar en un json en el root folder donde este nuestor script cart_to_csv.js
2. Ejecutar el script cart_to_csv con el parametro del nombre del json o sin ningun parametro
el default es cart.json

## Que hace el script?
De cada item del carrito extrae la siguiente informacion:
* qty
* item?id
* product_id
* product_name
* product_url
* product_price_value
* product_image

Y la guarda en un csv para abrirlo en excel y en un nuevo json simplificado.