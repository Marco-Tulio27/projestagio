print('sequencia fibonacci'.upper())
print('-'*50)
n=int(input('quantos termos quer mostrar? '))
t1=0
t2=1
print(t1,t2,end=' ')
cont=3
while cont <=n:
    t3=t1+t2
    print(t3,end=' ')
    t1=t2
    t2=t3
    cont+=1
#algoritimo desenvolvido em python
#nome=input('digite um nome que deseja ler o seu inverso: ')
#print(nome[::-1])