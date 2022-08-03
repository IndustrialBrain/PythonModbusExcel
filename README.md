# PythonModbusExcel
Coleta informações do CLP via Modbus e escreve em um arquivo no excel de acordo com um bit habilita.

Utilizado biblioteca Pandas e pyModbusTCP 0.2.0.
Construimos um software de CLP utilizando o CodeSys para escrever valores em registros. Existe um bit habita que dispara o evento para o Python salvar os registros lidos no excel.
Após confirmado a escrita, o Python escreve zero no registro no CLP e ficará aguardando uma nova solicitação de escrita.
OBS: O Software de CLP criado no CodeSys possui o nome de Modbus_Excel.project e está disponível neste repositório....
