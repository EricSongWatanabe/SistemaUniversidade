# ERIC SONG WATANABE - 22.125.086-3
# VICTOR PIMENTEL LARIO - 22.125.064-0

import pandas as pd
from faker import Faker
from sqlalchemy import create_engine
import random

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


fake = Faker('pt_BR')

nomes_cursos = [
    'Engenharia de Software', 'Ciência da Computação', 'Sistemas de Informação',
    'Engenharia Elétrica', 'Matemática Aplicada',
    'Ciência de Dados', 'Análise e Desenvolvimento de Sistemas',
    'Engenharia Aeroespacial', 'Cibersegurança'
]
cursos = [{'ID_Curso': i, 'Nome': nomes_cursos[i - 1]} for i in range(1, len(nomes_cursos) + 1)]
df_cursos = pd.DataFrame(cursos)
df_cursos.columns = df_cursos.columns.str.lower()
df_cursos.to_sql('cursos', engine, if_exists='append', index=False)
df_cursos.to_csv('cursos.csv', index=False)

departamentos = [{'ID_Departamento': i, 'Nome': f'Departamento {i}'} for i in range(1, 6)]
df_departamentos = pd.DataFrame(departamentos)
df_departamentos.columns = df_departamentos.columns.str.lower()
df_departamentos.to_sql('departamentos', engine, if_exists='append', index=False)
df_departamentos.to_csv('departamentos.csv', index=False)

nomes_disciplinas = [
    'Algoritmos', 'Banco de Dados', 'Estrutura de Dados',
    'Redes de Computadores', 'Compiladores', 'Inteligência Artificial',
    'Matemática Discreta', 'Cálculo I', 'Lógica de Programação', 'Engenharia de Software'
]
disciplinas = []
for i in range(1, 11):
    disciplinas.append({
        'ID_disciplina': i,
        'Nome': nomes_disciplinas[i - 1],
        'ID_Departamento': random.choice(departamentos)['ID_Departamento']
    })
df_disciplinas = pd.DataFrame(disciplinas)
df_disciplinas.columns = df_disciplinas.columns.str.lower()
df_disciplinas.to_sql('disciplinas', engine, if_exists='append', index=False)
df_disciplinas.to_csv('disciplinas.csv', index=False)

turmas = []
for i in range(1, 11):
    turmas.append({
        'ID_Turma': i,
        'Semestre': random.choice(['2023/1', '2023/2', '2024/1']),
        'Disciplina': random.choice(nomes_disciplinas),
        'Horario': random.choice(['08:00-10:00', '10:00-12:00', '14:00-16:00'])
    })
df_turmas = pd.DataFrame(turmas)
df_turmas.columns = df_turmas.columns.str.lower()
df_turmas.to_sql('turmas', engine, if_exists='append', index=False)
df_turmas.to_csv('turmas.csv', index=False)

alunos = []
for i in range(1, 101):
    alunos.append({
        'ID_Aluno': i,
        'Nome': fake.name(),
        'ID_Turma': random.choice(turmas)['ID_Turma'],
        'ID_Curso': random.choice(cursos)['ID_Curso']
    })
df_alunos = pd.DataFrame(alunos)
df_alunos.columns = df_alunos.columns.str.lower()
df_alunos.to_sql('alunos', engine, if_exists='append', index=False)
df_alunos.to_csv('alunos.csv', index=False)

professores = []
for i in range(1, 11):
    professores.append({
        'ID_Professor': i,
        'Nome': fake.name(),
        'CPF': fake.cpf(),
        'ID_Departamento': random.choice(departamentos)['ID_Departamento'],
        'ID_disciplina': random.choice(disciplinas)['ID_disciplina']
    })
df_professores = pd.DataFrame(professores)
df_professores.columns = df_professores.columns.str.lower()
df_professores.to_sql('professores', engine, if_exists='append', index=False)
df_professores.to_csv('professores.csv', index=False)

curso_disciplina = []
for _ in range(1, 21):
    curso_disciplina.append({
        'ID_Curso': random.choice(cursos)['ID_Curso'],
        'ID_disciplina': random.choice(disciplinas)['ID_disciplina']
    })
df_curso_disciplina = pd.DataFrame(curso_disciplina).drop_duplicates()
df_curso_disciplina.columns = df_curso_disciplina.columns.str.lower()
df_curso_disciplina.to_sql('curso_disciplina', engine, if_exists='append', index=False)
df_curso_disciplina.to_csv('curso_disciplina.csv', index=False)

turma_disciplina = []
for _ in range(1, 21):
    turma_disciplina.append({
        'ID_Turma': random.choice(turmas)['ID_Turma'],
        'ID_disciplina': random.choice(disciplinas)['ID_disciplina']
    })
df_turma_disciplina = pd.DataFrame(turma_disciplina).drop_duplicates()
df_turma_disciplina.columns = df_turma_disciplina.columns.str.lower()
df_turma_disciplina.to_sql('turma_disciplina', engine, if_exists='append', index=False)
df_turma_disciplina.to_csv('turma_disciplina.csv', index=False)

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
df_historico = pd.DataFrame(historico)
df_historico.columns = df_historico.columns.str.lower()
df_historico.to_sql('historicos_escolares', engine, if_exists='append', index=False)
df_historico.to_csv('historicos_escolares.csv', index=False)

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
df_tcc = pd.DataFrame(tccs)
df_tcc.columns = df_tcc.columns.str.lower()
df_tcc.to_sql('tcc', engine, if_exists='append', index=False)
df_tcc.to_csv('tcc.csv', index=False)
