# ERIC SONG WATANABE - 22.125.086-3
# VICTOR PIMENTEL LARIO - 22.125.064-0

import pandas as pd
from faker import Faker
from sqlalchemy import create_engine
import random

# Conexão com o Supabase
USER = "postgres.kntawsrthzfchoknasli"
PASSWORD = "bancodedados"
HOST = "aws-0-sa-east-1.pooler.supabase.com"
PORT = "5432"
DBNAME = "postgres"

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        print("Conectado com o Supabase")
except Exception as e:
    print("Erro ao conectar:")
    print(e)

fake = Faker('pt_BR')

# with engine.connect() as conn:
#     conn.execute("DELETE FROM tcc")
#     conn.execute("DELETE FROM historicos_escolares")
#     conn.execute("DELETE FROM turma_disciplina")
#     conn.execute("DELETE FROM curso_disciplina")
#     conn.execute("DELETE FROM professores")
#     conn.execute("DELETE FROM alunos")
#     conn.execute("DELETE FROM turmas")
#     conn.execute("DELETE FROM disciplinas")
#     conn.execute("DELETE FROM departamentos")
#     conn.execute("DELETE FROM cursos")

# cursos
nomes_cursos = [
    'Engenharia de Software', 'Ciência da Computação', 'Sistemas de Informação',
    'Engenharia Elétrica', 'Matemática Aplicada',
    'Ciência de Dados', 'Análise e Desenvolvimento de Sistemas',
    'Engenharia Aeroespacial', 'Cibersegurança'
]
cursos = [{'ID_Curso': i, 'Nome': nome} for i, nome in enumerate(nomes_cursos, start=1)]
df_cursos = pd.DataFrame(cursos).rename(columns=str.lower)
df_cursos.to_sql('cursos', engine, if_exists='append', index=False)

#departamentos reais
nomes_departamentos = [
    'Departamento de Computação',
    'Departamento de Matemática',
    'Departamento de Engenharia',
    'Departamento de Ciências de Dados',
    'Departamento de Sistemas de Informação'
]
departamentos = [{'ID_Departamento': i, 'Nome': nome} for i, nome in enumerate(nomes_departamentos, start=1)]
df_departamentos = pd.DataFrame(departamentos).rename(columns=str.lower)
df_departamentos.to_sql('departamentos', engine, if_exists='append', index=False)

#disciplinas associadas a departamentos específicos
disciplinas_por_departamento = {
    1: ['Algoritmos', 'Estrutura de Dados', 'Compiladores'],
    2: ['Matemática Discreta', 'Cálculo I'],
    3: ['Redes de Computadores', 'Engenharia de Software'],
    4: ['Inteligência Artificial', 'Banco de Dados'],
    5: ['Lógica de Programação']
}
disciplinas = []
disc_id = 1
for id_dep, nomes in disciplinas_por_departamento.items():
    for nome in nomes:
        disciplinas.append({
            'ID_Disciplina': disc_id,
            'Nome': nome,
            'ID_Departamento': id_dep
        })
        disc_id += 1
df_disciplinas = pd.DataFrame(disciplinas).rename(columns=str.lower)
df_disciplinas.to_sql('disciplinas', engine, if_exists='append', index=False)

#turmas
turmas = []
for i in range(1, 11):
    turmas.append({
        'ID_Turma': i,
        'Semestre': random.choice(['2023/1', '2023/2', '2024/1']),
        'Disciplina': random.choice(df_disciplinas['nome']),
        'Horario': random.choice(['08:00-10:00', '10:00-12:00', '14:00-16:00'])
    })
df_turmas = pd.DataFrame(turmas).rename(columns=str.lower)
df_turmas.to_sql('turmas', engine, if_exists='append', index=False)

# alunos
alunos = []
for i in range(1, 101):
    alunos.append({
        'ID_Aluno': i,
        'Nome': fake.name(),
        'ID_Turma': random.choice(turmas)['ID_Turma'],
        'ID_Curso': random.choice(cursos)['ID_Curso']
    })
df_alunos = pd.DataFrame(alunos).rename(columns=str.lower)
df_alunos.to_sql('alunos', engine, if_exists='append', index=False)

#professores
professores = []
for i in range(1, 11):
    prof_disc = random.choice(disciplinas)
    prof_dep = next((d['ID_Departamento'] for d in departamentos if d['ID_Departamento'] == prof_disc['ID_Departamento']), 1)
    professores.append({
        'ID_Professor': i,
        'Nome': fake.name(),
        'CPF': fake.cpf(),
        'ID_Departamento': prof_dep,
        'ID_Disciplina': prof_disc['ID_Disciplina']
    })
df_professores = pd.DataFrame(professores).rename(columns=str.lower)
df_professores.to_sql('professores', engine, if_exists='append', index=False)

#curso x disciplina
curso_disciplina = []
for _ in range(30):
    curso_disciplina.append({
        'ID_Curso': random.choice(cursos)['ID_Curso'],
        'ID_Disciplina': random.choice(disciplinas)['ID_Disciplina']
    })
df_curso_disciplina = pd.DataFrame(curso_disciplina).drop_duplicates().rename(columns=str.lower)
df_curso_disciplina.to_sql('curso_disciplina', engine, if_exists='append', index=False)

# turma x disciplina
turma_disciplina = []
for _ in range(30):
    turma_disciplina.append({
        'ID_Turma': random.choice(turmas)['ID_Turma'],
        'ID_Disciplina': random.choice(disciplinas)['ID_Disciplina']
    })
df_turma_disciplina = pd.DataFrame(turma_disciplina).drop_duplicates().rename(columns=str.lower)
df_turma_disciplina.to_sql('turma_disciplina', engine, if_exists='append', index=False)

#historico escolar
historico = []
for i in range(1, 101):
    aluno = random.choice(alunos)
    disciplina = random.choice(disciplinas)
    historico.append({
        'ID_Historico': i,
        'Semestre': random.choice(['2023/1', '2023/2', '2024/1']),
        'Nota': random.randint(0, 100),
        'Situacao': random.choice(['Aprovado', 'Reprovado', 'Trancado']),
        'Curso': random.choice(cursos)['Nome'],
        'Disciplina': disciplina['Nome'],
        'ID_Aluno': aluno['ID_Aluno']
    })
df_historico = pd.DataFrame(historico).rename(columns=str.lower)
df_historico.to_sql('historicos_escolares', engine, if_exists='append', index=False)

#TCC
tccs = []
for i in range(1, 21):
    tccs.append({
        'ID_TCC': i,
        'Titulo': fake.sentence(nb_words=6),
        'Curso': random.choice(cursos)['Nome'],
        'Finalizado': random.choice([True, False]),
        'Ano_Conclusao': random.choice([2023, 2024]),
        'ID_Aluno': random.choice(alunos)['ID_Aluno'],
        'ID_Professor': random.choice(professores)['ID_Professor']
    })
df_tcc = pd.DataFrame(tccs).rename(columns=str.lower)
df_tcc.to_sql('tcc', engine, if_exists='append', index=False)
