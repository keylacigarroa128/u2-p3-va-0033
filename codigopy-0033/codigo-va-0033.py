# Keyla Paola Cigarroa Palacios NC = 0033
import cv2
import matplotlib.pyplot as plt
import os
#ruta de la imagen
ruta_imagen = os.path.join(
    "img-original-0033",
    "img-licuadora-0033.jpg"
)
#imagen
# Vamos a crear nuestra matriz principal 
licuadora = cv2.imread(ruta_imagen)
print(licuadora)
#convertir de BGR a RGB color rojo COLOR_BGR2RGB
img = cv2.cvtColor(licuadora, cv2.COLOR_BGR2RGB)
cv2.imshow("licuadora original 0033", licuadora)
cv2.waitKey(0) # tiempo de espera
cv2.destroyAllWindows() # Destruye todas las ventanas en memoria 

print("Keyla Paola Cigarroa Palacios NC = 0033")        
