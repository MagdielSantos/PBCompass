CREATE VIEW fato_locacao AS
SELECT
  idLocacao,
  idCliente,
  idCarro,
  idVendedor,
  idCombustivel,
  horaLocacao,
  qtdDiaria,
  vlrDiaria,
  dataEntrega,
  horaEntrega
FROM tb_locacao;

CREATE VIEW dim_cliente AS
SELECT
  idCliente,
  nomeCliente,
  cidadeCliente,
  estadoCliente,
  paisCliente
FROM tb_cliente;

CREATE VIEW dim_carro AS
SELECT
  idCarro,
  kmCarro,
  classiCarro,
  marcaCarro,
  modeloCarro,
  anoCarro,
  idCombustivel
FROM tb_carro;

CREATE VIEW dim_combustivel AS
SELECT
  idCombustivel,
  tipoCombustivel
FROM tb_combustivel;

CREATE VIEW dim_vendedor AS
SELECT
  idVendedor,
  nomeVendedor,
  sexoVendedor,
  estadoVendedor
FROM tb_vendedor;
