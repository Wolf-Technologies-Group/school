# -*- coding: utf-8 -*-
#13/12/2015
#Creator Victor Consuegra - "Sagaz.Wolf"
#consuegra177@gmail.com
#Calculadora de media escolares
#Entre com o valor solicitado

print
print
print
print '======================================================'
print 'Calculadora de média escolares !'
print '------------------------------------------------------'
print 'Apenas números inteiros ou decimais.'
print
media_bim1 = float (raw_input('Qual foi a sua média no 1° bimestre ?   '))
media_bim2 = float (raw_input('Qual foi a sua média no 2° bimestre ?   '))
media_bim3 = float (raw_input('Qual foi a sua média no 3° bimestre ?   '))
print '------------------------------------------------------'
print
total = media_bim1 + media_bim2 + media_bim3
media = total/3
print '------------------------------------------------------'
print "A soma total das suas notas foram de: %.2f  " % total
print 'A sua media de notas é de : %1.2f  ' % media  #Esta linha tem um exemplo importante sobre o poderoso sinal '%' , olho no %1.2f
print '------------------------------------------------------'
if media <= 4.70 :
    print 'Suas notas estão RUINS , existe uma  chance de você não passar este ano !'
elif media >= 6.70 :
    print 'Você PASSOU ! aproveite as férias !'
else:
    media >= 5.25
    print 'Suas notas estão BOAS ! existe uma boa chance de você passar. Parabéns !!'
print '------------------------------------------------------'
print
print 'Fim do programa'
print '======================================================'
