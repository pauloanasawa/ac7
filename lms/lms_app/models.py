from django.db import models

# Create your models here.
class Professor(models.Model):
    def __str__(self):
        return "Nome: " + self.nome + " - Email: " + self.email #teste 01

    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    login = models.TextField(max_length=20)
    senha = models.TextField(max_length=20)

    def save(self): ## teste 02
        if self.login == '':
             raise Exception('Professor sem login')
        super(Professor,self).save()

    
    def save(self):    #test 03
        print('estou salvando!')
        if(self.login == ''):
            raise Exception('login nao enviado')
        if(self.email == ''):
            self.email = "email nao fornecido"
        super(Professor,self).save()

#teste 4
    def save(self):
        if self.login =='':
            raise Exception('professor sem login')
        if self.email == '':
            self.email == 'email nao fornecido'
        professor.login = Professor.objects.filter(login=self.login)
        if len(professor.login)>0:
            raise Exception('login já utilizado')
        super(Professor,self).save()
        


#teste 5 

class Disciplina(models.Model):
    def _str_(self):
        return 'Nome' + self.nome + 'Ementa' + self.ementa

    nome = models.TextField(max_length=50)
    ementa = models.TextField(max_length=5000)

    
#teste 6

    def save(self):
        if self.nome =='':
            raise Exception('disciplina sem nome')
        disciplina.nome = Disciplina.objects.filter(nome=self.nome)
        if len(disciplina.nome) > 0:
            raise Exception('Disciplina já cadastrada !')
        super(Disciplina,self).save()
        
        

#teste 7
class DisciplinaOfertada(models.Model):
    
    def _str_(self):
        return 'Curso' + self.curso + 'Ano' + self.ano + 'Semestre' + self.semestre + 'Turma' + self.turma + 'Professor' + self.professor  + 'Disciplina' + self.disciplina

    curso = models.TextField(max_length=255)
    turma = models.TextField(max_length=5)
    ano = models.IntegerField() #um inteiro, representa um ano
    semestre = models.IntegerField() #um inteiro, 1 para primeiro sem e 2 para segundo
    professor = models.IntegerField() #id de um professor valido
    disciplina = models.IntegerField() #id de uma disciplina valida



#teste 8

    def save(self):
        if self.curso == '':
            raise Exception('curso não informado !!')
        ofertada.curso = DisciplinaOfertada.objects.filter(curso=self.curso)
        if len(ofertada.curso) and not 'ADS' or not 'SI' or not 'BD':
            raise Exception('curso não existente!!')
        super(DisciplinaOfertada,self).save()

        
        
        
#teste 09    
        
    def save(self):
        if self.curso == '':
            raise Exception('digite o nome do curso..')
        ofertada.curso = DisciplinaOfertada.objects.filter(curso=self.curso)
        ofertada.ano = DisciplinaOfertada.objects.filter(curso=self.ano)
        ofertada.semestre = DisciplinaOfertada.objects.filter(curso=self.semestre)
        ofertada.turma = DisciplinaOfertada.objects.filter(curso=self.turma)
        ofertada.professor = DisciplinaOfertada.objects.filter(curso=self.professor)
        ofertada.disciplina = DisciplinaOfertada.objects.filter(curso=self.disciplina)

        if len(ofertada.curso) >0 and len(ofertada.ano) > 0 and len(ofertada.semestre) > 0 and len(ofertada.turma) > 0 and len(ofertada.professor) > 0 and len(ofertada.professor) > 0:
            raise Exception('Disciplina já cadastrada')
        super(DisciplinaOfertada,self).save()

        
        
        
        
        
       