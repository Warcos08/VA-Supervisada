import csv
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle

import preproceso, train
import test

import warnings
warnings.filterwarnings('ignore')

def entrenamiento():
    dfTrain = pd.read_csv("datasets/data.csv")

    """ # Para entrenar con todo el train
    dfDev = pd.read_csv("datasets/dev.csv")
    frames = [dfTrain, dfDev]
    dfTrain = pd.concat(frames)"""

    eleccion = int(input('''Elija el preproceso deseado para la prueba:
                            (1) BOW
                            (2) Topic Modeling
                            (3) Salir\n'''))

    # Aplico el preproceso al train
    if eleccion == 1:
        print("Ha elegido BOW")
        #dfTrain = preproceso.bowTrain(dfTrain)
        dfTrain = pd.read_csv("datasets/bow/trainBOW.csv")

    elif eleccion == 2:
        print("Ha elegido Topic Modeling")
        #num_topics = int(input("Introduzca el numero de topicos deseado (óptimo --> 26): \n"))
        num_topics = 26
        #dfTrain = preproceso.topicosTrain(dfTrain, num_topics)
        dfTrain = pd.read_csv("datasets/lda/trainLDA.csv")


    elif eleccion == 3:
        print("Saliendo . . .")
        return

    else:
        print("Seleccion incorrecta")
        entrenamiento()



    eleccion = int(input('''Elija el modelo a entrenar:
                                (1) SVM
                                (2) LightGBM
                                (3) Salir\n'''))


    # Entreno el modelo elegido
    if eleccion == 1:
        print("Ha elegido SVM")
        train.trainSVM(dfTrain)

    elif eleccion == 2:
        print("Ha elegido LightGBM")
        train.trainLightGBM(dfTrain)

    elif eleccion == 3:
        print("Saliendo . . .")
        return

    else:
        print("Seleccion incorrecta")
        print("Saliendo . . .")
        return


def testeo():
    # La parte de test cambia segun el preproceso empleado para el train
    dfTest = pd.read_csv("datasets/dev.csv")
    """defTest = pd.read_csv("datasets/test.csv")"""

    eleccion = int(input('''Elija el preproceso deseado para el test (debe ser el mismo que el empleado para el train):
                            (1) BOW
                            (2) Topic Modeling
                            (3) Salir\n'''))

    # Aplico el preproceso al train
    if eleccion == 1:
        print("Ha elegido BOW")
        #dfTest = preproceso.bowTest(dfTest)
        dfTest = pd.read_csv("datasets/bow/testBOW.csv")


    elif eleccion == 2:
        print("Ha elegido Topic Modeling")
        #dfTest = preproceso.topicosTest(dfTest)
        dfTest = pd.read_csv("datasets/lda/testLDA.csv")


    elif eleccion == 3:
        print("Saliendo . . .")
        return

    else:
        print("Seleccion incorrecta")
        testeo()

    eleccion = int(input('''Elija el modelo a testear:
                                    (1) SVM
                                    (2) LightGBM
                                    (3) Salir\n'''))

    # Entreno el modelo elegido
    if eleccion == 1:
        print("Ha elegido SVM")
        test.testSVM(dfTest)

    elif eleccion == 2:
        print("Ha elegido LightGBM")
        test.testLightGBM(dfTest)

    elif eleccion == 3:
        print("Saliendo . . .")
        return

    else:
        print("Seleccion incorrecta")
        print("Saliendo . . .")
        return


def main():
    print('''\n\nBIENVENIDO AL AGRUPADOR DE DOCUMENTOS MÉDICOS
    
        Pulse el número según lo que que desee ejecutar:
            (1) Entrenar el modelo 
            (2) Testear un modelo previamente entrenado
            (3) Salir

        Por Marcos Merino\n''')

    eleccion = int(input())

    if eleccion == 1:
        print("Ha elegido entrenar un modelo")
        entrenamiento()
        main()

    elif eleccion == 2:
        print("Ha elegido testear un modelo ")
        testeo()
        main()

    elif eleccion == 3:
        print("SALIENDO...")
        return

    else:
        print("Seleccion incorrecta\n\n")
        main()

if __name__ == '__main__':
    main()



