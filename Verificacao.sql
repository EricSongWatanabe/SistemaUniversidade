-- ERIC SONG WATANABE - 22.125.086-3
-- VICTOR PIMENTEL LARIO - 22.125.064-0

-- alunos com turma inexistente
SELECT * 
FROM alunos
WHERE id_turma NOT IN (SELECT id_turma FROM turmas);

-- alunos com curso inexistente
SELECT * 
FROM alunos
WHERE id_curso NOT IN (SELECT id_curso FROM cursos);

-- professores com departamento inexistente
SELECT * 
FROM professores
WHERE id_departamento NOT IN (SELECT id_departamento FROM departamentos);

-- professores com disciplina inexistente
SELECT * 
FROM professores
WHERE id_disciplina NOT IN (SELECT id_disciplina FROM disciplinas);

-- disciplinas com departamento inexistente
SELECT * 
FROM disciplinas
WHERE id_departamento NOT IN (SELECT id_departamento FROM departamentos);

-- curso_Disciplina com curso inexistente
SELECT * 
FROM curso_disciplina
WHERE id_curso NOT IN (SELECT id_curso FROM cursos);

-- curso_Disciplina com disciplina inexistente
SELECT * 
FROM curso_disciplina
WHERE id_disciplina NOT IN (SELECT id_disciplina FROM disciplinas);

-- turma_Disciplina com turma inexistente
SELECT * 
FROM turma_disciplina
WHERE id_turma NOT IN (SELECT id_turma FROM turmas);

-- turma_Disciplina com disciplina inexistente
SELECT * 
FROM turma_disciplina
WHERE id_disciplina NOT IN (SELECT id_disciplina FROM disciplinas);

-- historicos_Escolares com aluno inexistente
SELECT * 
FROM historicos_escolares
WHERE id_aluno NOT IN (SELECT id_aluno FROM alunos);

-- TCC com aluno inexistente
SELECT * 
FROM tcc
WHERE id_aluno NOT IN (SELECT id_aluno FROM alunos);

-- TCC com professor inexistente
SELECT * 
FROM tcc
WHERE id_professor NOT IN (SELECT id_professor FROM professores);