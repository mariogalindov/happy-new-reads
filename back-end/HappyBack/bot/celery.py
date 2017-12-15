from __future__ import absolute_import
import os
 
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HappyBack.settings') #estamos configurando la variable de 
                                        #entorno ‘DJANGO_SETTINGS_MODULE’ para que tome / use el modulo de configuración 
                                        #que le estamos pasando en este caso el unico que tenemos ‘HappyBack.settings‘.
from django.conf import settings    #mportar nuestro archivo de configuracion pero via Django
app = Celery('CeleryApp') #Creamos la aplicacion Cerery
app.config_from_object('django.conf:settings') # Inicializamos nuestra app celery con la configuración de nuestro proyecto Django
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS) #Celery auto-inspeccionara nuestras app y buscara metodos con la anotación ‘@tasks’ de celery.
app.conf.update(
    BROKER_URL = 'django://', 
)