    CREATE TABLE tb_locacao (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idVendedor INT,
    idCarro INT,
    qtdDiaria INT,
    vlrDiaria DECIMAL(18, 2),
    horaLocacao TIME,
    dataEntrega DATE,
    horaEntrega TIME,
    FOREIGN KEY (idCliente) REFERENCES tb_cliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES tb_carro(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES tb_vendedor(idVendedor)
);

CREATE TABLE tb_cliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40)
);

CREATE TABLE tb_carro (
    idCarro INT PRIMARY KEY,
    idCombustivel INT,
    modeloCarro VARCHAR(80),
    marcaCarro VARCHAR(80),
    kmCarro INT,
    anoCarro INT,
    classiCarro VARCHAR(50),
    FOREIGN KEY (idCombustivel) REFERENCES tb_combustivel(idCombustivel)
);

CREATE TABLE tb_combustivel (
    idCombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20)
);

CREATE TABLE tb_vendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(15),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(40)
);