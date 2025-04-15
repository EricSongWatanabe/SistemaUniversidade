-- ERIC SONG WATANABE - 22.125.086-3
-- VICTOR PIMENTEL LARIO - 22.125.064-0

CREATE TABLE Departamentos (
    ID_Departamento INT PRIMARY KEY,
    Nome VARCHAR(100)
);

CREATE TABLE Disciplinas (
    ID_disciplina INT PRIMARY KEY,
    Nome VARCHAR(100),
    ID_Departamento INT,
    FOREIGN KEY (ID_Departamento) REFERENCES Departamentos(ID_Departamento)
);

CREATE TABLE Cursos (
    ID_Curso INT PRIMARY KEY,
    Nome VARCHAR(100)
);

CREATE TABLE Turmas (
    ID_Turma INT PRIMARY KEY,
    Semestre VARCHAR(10),
    Disciplina VARCHAR(100),
    Horario VARCHAR(50)
);

CREATE TABLE Alunos (
    ID_Aluno INT PRIMARY KEY,
    Nome VARCHAR(100),
    ID_Turma INT,
    ID_Curso INT,
    FOREIGN KEY (ID_Turma) REFERENCES Turmas(ID_Turma),
    FOREIGN KEY (ID_Curso) REFERENCES Cursos(ID_Curso)
);

CREATE TABLE Professores (
    ID_Professor INT PRIMARY KEY,
    Nome VARCHAR(100),
    CPF VARCHAR(14),
    ID_Departamento INT,
    ID_disciplina INT,
    FOREIGN KEY (ID_Departamento) REFERENCES Departamentos(ID_Departamento),
    FOREIGN KEY (ID_disciplina) REFERENCES Disciplinas(ID_disciplina)
);

CREATE TABLE Curso_Disciplina (
    ID_Curso INT,
    ID_disciplina INT,
    PRIMARY KEY (ID_Curso, ID_disciplina),
    FOREIGN KEY (ID_Curso) REFERENCES Cursos(ID_Curso),
    FOREIGN KEY (ID_disciplina) REFERENCES Disciplinas(ID_disciplina)
);

CREATE TABLE Turma_Disciplina (
    ID_Turma INT,
    ID_disciplina INT,
    PRIMARY KEY (ID_Turma, ID_disciplina),
    FOREIGN KEY (ID_Turma) REFERENCES Turmas(ID_Turma),
    FOREIGN KEY (ID_disciplina) REFERENCES Disciplinas(ID_disciplina)
);

CREATE TABLE Historicos_Escolares (
    ID_Historico INT PRIMARY KEY,
    Semestre VARCHAR(10),
    Nota INT,
    Situacao VARCHAR(50),
    Curso VARCHAR(100),
    Disciplina VARCHAR(100),
    ID_Aluno INT,
    FOREIGN KEY (ID_Aluno) REFERENCES Alunos(ID_Aluno)
);

CREATE TABLE TCC (
    ID_TCC INT PRIMARY KEY,
    Titulo VARCHAR(200),
    Curso VARCHAR(100),
    Finalizado BOOLEAN,
    Ano_Conclusao INT,
    ID_Aluno INT,
    ID_Professor INT,
    FOREIGN KEY (ID_Aluno) REFERENCES Alunos(ID_Aluno),
    FOREIGN KEY (ID_Professor) REFERENCES Professores(ID_Professor)
);
