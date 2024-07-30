create database campeonato; -- cria o banco de dados 
-- começar com tabelas que nao tenham FKs
create table modalidade(
    idModalidade int(5) not null,
    nome varchar(30) not null,  -- explicação dos tipos de var's: https://www.w3schools.com/sql/sql_datatypes.asp
    treinador varchar(50) not null,
    primary key(idModalidade),
)
create table atleta(
    codigo int(5) not null,
    nome varchar(50) not null,
    peso float(5,2) not null,
    altura float(3,2) not null,
    codmodalidade int(5) not null,
    primary key(codigo),
    foreign key(codmodalidade) references modalidade(idModalidade)  --conecta com uma coluna de uma outra tabela (precisa ser PK)
    ); --serve só pra 'conectar' as duas, ainda não dá pra fazer nada, mas quer dizer que estão interligadas.
    
    create table competicao(
        codigo int(5) not null,
        datinha date not null,
        ocal varchar(50) not null,
        cidade varchar(50) not null,
        estado char(2) not null,
        codatleta int(5) not null,
        primary key(codigo),
        foreign key(codatleta) references atleta(codigo)); -- lembrar da lógica disso depois tb
    -----------

    -- exemplo inserir campo
    alter table modalidade
    add preparador varchar(50) not null;
    -- exemplo remover campo
    alter table modalidade
    drop preparador;
    -- exemplo alterar campo
    alter table modalidade
    alter treinador varchar(100) not null; -- muda o tamanho da varchar
    alter treinador set preparador varchar(100) not null; -- trocar o nome de treinador pra preparador (alterei o nome do campo)
    -- excluir tabela
    drop table modalidade;
    -- excluir database
    drop campeonato;
