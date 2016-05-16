# -*- coding: utf-8 -*-
#!/usr/bin/python


#####13/12/2015#####
######Creator Victor Consuegra #####
######consuegra177@gmail.com######


# Adicionando funções

import os
import sys

# Hora atual

from   datetime import datetime
now =  datetime.now()


#Criando funções

# Banner do script

def banner ():
    print '''
                      _____      _                 _
                     / ____|    | |               | |
                    | (___   ___| |__   ___   ___ | |
                     \___ \ / __| '_ \ / _ \ / _ \| |
                     ____) | (__| | | | (_) | (_) | |
                    |_____/ \___|_| |_|\___/ \___/|_|
'''
print

# Função hora atual


def hora():
    print " Brasília, %s / %s / %s  at %.2f  " % (now.day, now.month, now.year, now.hour)
    print '--' * 81

# Chamando as funções dentro do código

banner()
hora()

# Criando as variáveis

def menu():
    print " # Calculadora de médias escolares"
    print " # Entre com as suas médias do 1°,2° e 3° bimestre "
    print " # Para sair do programa digite [0] "
    print

    media_1      = float (raw_input ( " Digite sua nota do 1° bimestre   "))
    media_2      = float (raw_input ( " Digite sua nota do 2° bimestre   "))
    media_3      = float (raw_input ( " Digite sua nota do  3° bimestre   "))

# Cálculo

    total_media  = (media_1 + media_2 + media_3)
    total_media3 =  (total_media / 3)

#Exibindo os resultados

    print
    print "  A sua média de 3 bimestres é de  %.2f           "  % total_media3
    print "  O total de nota obtida em 3 bimestres é  %.2f   "  % total_media
    print
    hora()

# Comandos de decisão

    if   total_media   <= 10 :
        print '--' * 81
        print " Você tem poucas chances de passar este ano  "
    elif total_media <= 10.2 :
        print '--' * 81
        print " Você tem boas chances de passar este ano    "
    elif total_media >= 20 :
        print '--' * 81
        print " Você já passou de ano ! "
        print
    else:
        sys.exit()
print

# Chamando a função menu dentro do código

menu() # Se retirar este comando do código, nada mais faz sentido


