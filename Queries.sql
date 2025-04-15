-- ERIC SONG WATANABE - 22.125.086-3
-- VICTOR PIMENTEL LARIO - 22.125.064-0

--1 Mostre todo o histórico escolar de um aluno que teve reprovação em uma disciplina, retornando inclusive a reprovação em um semestre e a aprovação no semestre seguinte.

SELECT 
    h1.ID_Aluno,
    h1.Disciplina,
    h1.Semestre AS Semestre_Reprovacao,
    h1.Nota AS Nota_Reprovacao,
    h2.Semestre AS Semestre_Aprovacao,
    h2.Nota AS Nota_Aprovacao
FROM Historicos_Escolares h1
JOIN Historicos_Escolares h2 ON h1.ID_Aluno = h2.ID_Aluno AND h1.Disciplina = h2.Disciplina
WHERE 
    h1.Situacao = 'Reprovado' 
    AND h2.Situacao = 'Aprovado'
    AND h1.Semestre < h2.Semestre;

--2 Mostre todos os TCCs orientados por um professor junto com os nomes dos alunos que fizeram o projeto.

SELECT 
    p.Nome AS Professor,
    a.Nome AS Nome_Aluno,
    t.Titulo AS Titulo_TCC,
    t.Ano_Conclusao
FROM TCC t
JOIN Professores p ON t.ID_Professor = p.ID_Professor
JOIN Alunos a ON t.ID_Aluno = a.ID_Aluno
WHERE 
    p.Nome = 'Prof. João';

--3 Mostre a matriz curicular de pelo menos 2 cursos diferentes que possuem disciplinas em comum (e.g., Ciência da Computação e Ciência de Dados). Este exercício deve ser dividido em 2 queries sendo uma para cada curso.

SELECT 
    c.Nome AS Curso,
    d.ID_disciplina,
    d.Nome AS Disciplina
FROM Curso_Disciplina cd
LEFT JOIN Cursos c ON cd.ID_Curso = c.ID_Curso
LEFT JOIN Disciplinas d ON cd.ID_disciplina = d.ID_disciplina
WHERE 
    c.Nome = 'Sistemas de Informação';

SELECT 
    c.Nome AS Curso,
    d.ID_disciplina,
    d.Nome AS Disciplina
FROM Curso_Disciplina cd
LEFT JOIN Cursos c ON cd.ID_Curso = c.ID_Curso
LEFT JOIN Disciplinas d ON cd.ID_disciplina = d.ID_disciplina
WHERE 
    c.Nome = 'Engenharia da Computação';

--4 Para um determinado aluno, mostre os códigos e nomes das diciplinas já cursadas junto com os nomes dos professores que lecionaram a disciplina para o aluno.

SELECT 
    a.Nome AS Aluno,
    d.ID_disciplina,
    d.Nome AS Disciplina,
    p.Nome AS Professor
FROM Historicos_Escolares h
JOIN Alunos a ON h.ID_Aluno = a.ID_Aluno
JOIN Disciplinas d ON h.Disciplina = d.Nome
JOIN Professores p ON d.ID_disciplina = p.ID_disciplina
WHERE 
    a.ID_Aluno = 401;

--5 Liste todos os chefes de departamento e coordenadores de curso em apenas uma query de forma que a primeira coluna seja o nome do professor, a segunda o nome do departamento coordena e a terceira o nome do curso que coordena. Substitua os campos em branco do resultado da query pelo texto "nenhum".

SELECT 
    p.Nome AS Professor,
    COALESCE(d.Nome, 'nenhum') AS Departamento,
    COALESCE(c.Nome, 'nenhum') AS Curso
FROM Professores p
LEFT JOIN Departamentos d ON p.ID_Departamento = d.ID_Departamento
LEFT JOIN Cursos c ON p.ID_disciplina IN (SELECT ID_disciplina FROM Curso_Disciplina WHERE ID_Curso = c.ID_Curso);


--6 Encontre os nomes de todos os estudantes.
SELECT Nome
FROM Alunos;

--7 Liste os IDs e nomes de todos os professores.
SELECT id_professor, nome
FROM Professores;

--8 Encontre os nomes de todos os estudantes que cursaram "Banco de Dados"
SELECT DISTINCT a.Nome
FROM Historicos_Escolares h
JOIN Alunos a ON h.ID_Aluno = a.ID_Aluno
WHERE h.Disciplina = 'Banco de Dados';

--9 Encontre os estudantes que cursaram "Ciência da Computação" ou "Engenharia Elétrica".
SELECT a.Nome AS Aluno, c.Nome AS Curso
FROM Alunos a
JOIN Cursos c ON a.ID_Curso = c.ID_Curso
WHERE c.Nome IN ('Ciência da Computação', 'Engenharia Elétrica');

--10 Liste todos os cursos que foram cursados por estudantes do departamento 2 ou do departamento 3.
SELECT DISTINCT c.Nome AS Nome_Curso, dpt.Nome AS Nome_Departamento
FROM Cursos c
JOIN Alunos a ON c.ID_Curso = a.ID_Curso
JOIN Curso_Disciplina cd ON c.ID_Curso = cd.ID_Curso
JOIN Disciplinas d ON cd.ID_disciplina = d.ID_disciplina
JOIN Departamentos dpt ON d.ID_Departamento = dpt.ID_Departamento
WHERE d.ID_Departamento IN (2, 3);

--11 Recupere os nomes dos estudantes que cursaram disciplinas do departamento 2.
SELECT DISTINCT a.Nome AS Nome_Aluno
FROM Historicos_Escolares h
JOIN Alunos a ON h.ID_Aluno = a.ID_Aluno
JOIN Disciplinas d ON h.Disciplina = d.Nome
WHERE d.ID_Departamento = 2;

--12 Recupere os nomes dos estudantes que cursaram disciplinas em mais de 3 departamentos.
SELECT a.Nome AS Nome_Aluno
FROM Historicos_Escolares h
JOIN Alunos a ON h.ID_Aluno = a.ID_Aluno
JOIN Disciplinas d ON h.Disciplina = d.Nome
GROUP BY a.ID_Aluno, a.Nome
HAVING COUNT(DISTINCT d.ID_Departamento) > 3;

--13 Recupere os nomes dos estudantes que são orientados por um professor que ensina "Banco de Dados"
SELECT DISTINCT a.Nome AS Nome_Aluno
FROM Professores p
JOIN Disciplinas d ON p.ID_disciplina = d.ID_disciplina
JOIN Turma_Disciplina td ON d.ID_disciplina = td.ID_disciplina
JOIN Turmas t ON td.ID_Turma = t.ID_Turma
JOIN Alunos a ON a.ID_Turma = t.ID_Turma
WHERE d.Nome = 'Banco de Dados';

--14 Liste os nomes dos estudantes que não cursaram nenhum curso no departamento 3.
SELECT DISTINCT 
    a.Nome AS Nome_Aluno,
    dept.Nome AS Nome_Departamento
FROM Alunos a
JOIN Historicos_Escolares h ON a.ID_Aluno = h.ID_Aluno
JOIN Disciplinas d ON h.Disciplina = d.Nome
JOIN Departamentos dept ON d.ID_Departamento = dept.ID_Departamento
WHERE a.ID_Aluno NOT IN (
    SELECT h.ID_Aluno
    FROM Historicos_Escolares h
    JOIN Disciplinas d ON h.Disciplina = d.Nome
    WHERE d.ID_Departamento = 3
);

--15 Recupere os títulos dos cursos e os nomes dos professores que os ministraram, onde o curso tenha pelo menos 15 alunos matriculados.
SELECT DISTINCT 
    c.Nome AS Nome_Curso,
    p.Nome AS Nome_Professor
FROM Cursos c
JOIN Alunos a ON c.ID_Curso = a.ID_Curso
JOIN Curso_Disciplina cd ON c.ID_Curso = cd.ID_Curso
JOIN Disciplinas d ON cd.ID_disciplina = d.ID_disciplina
JOIN Professores p ON p.ID_disciplina = d.ID_disciplina
WHERE c.ID_Curso IN (
    SELECT ID_Curso
    FROM Alunos
    GROUP BY ID_Curso
    HAVING COUNT(*) >= 15
);