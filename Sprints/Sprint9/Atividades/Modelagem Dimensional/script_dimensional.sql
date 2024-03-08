CREATE TABLE fato_locacao (
  idLocacao       int primary key,
  idCliente       int,
  idCarro         int,
  idVendedor      int,
  idCombustivel   int,
  dataLocacao     datetime,
  horaLocacao     time,
  qtdDiaria       int,
  vlrDiaria       decimal(18,2),
  dataEntrega     date,
  horaEntrega     time,
  foreign key (idCliente) references dim_cliente(idCliente),
  foreign key (idCarro) references dim_carro(idCarro),
  foreign key (idVendedor) references dim_vendedor(idVendedor)
);

CREATE TABLE dim_cliente (
  idCliente       int primary key,
  nomeCliente     varchar(100),
  cidadeCliente   varchar(40),
  estadoCliente   varchar(40),
  paisCliente     varchar(40)
);

CREATE TABLE dim_carro (
  idCarro         int primary key,
  kmCarro         int,
  classiCarro     varchar(50),
  marcaCarro      varchar(80),
  modeloCarro     varchar(80),
  anoCarro        int,
  idCombustivel   int,
  foreign key (idCombustivel) references dim_combustivel(idCombustivel)
);

CREATE TABLE dim_combustivel (
  idCombustivel   int primary key,
  tipoCombustivel varchar(20)
);

CREATE TABLE dim_vendedor (
  idVendedor      int primary key,
  nomeVendedor    varchar(15),
  sexoVendedor    smallint,
  estadoVendedor  varchar(40)
);
