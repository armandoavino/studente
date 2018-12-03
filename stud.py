classi=[]
class Studente:
        def__init_-(self,nome,cognome,classe):
               self.nome=nome
               self.cognome=cognome
               self.classe=classe

#main
i=0
num= input("Questi studenti ci sono?")
num= int(num)
while i<num :
        nome= input ("Inserisci il nome dello studente= ")
        cognome= input ("Inserisci il cognome dello studente= ")
        classe= input ("Inserisci la classe dello studente in questione= ")
        Studenti=Studente(nome, cognome, classe)
        classe.append(Studenti)
        classi[i]= Studenti
        print (classi[i].nome, '//' ,classi[i].cognome, '//', classi[i].classe)
        i=i+1