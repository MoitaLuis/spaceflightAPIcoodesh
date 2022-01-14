******************************************************************************* fastAPI Backend for Coodesh *******************************************************************************

Aplicação desenvolvida para consumir a API Space Flight News de forma a cumprir os desafios propostos no processo seletivo da Coodesh

Principais Tecnologias:
    -Python
    -MongoDB
    -fastAPI

*************************************************************************************** Modo de uso ***************************************************************************************
Uso: Para inicialiazr o serviço são necessários 2 comandos: 
- uvicorn index:app --reload
- uvicorn cron:app --reload
Desta forma, os endpoints ficarão acesíveis e ao mesmo tempo será executada a atualização diária dos artigos às 09:00
Após inicializada a api estará acessível localmente e o banco de dados poderá ser acessado através dos endpoints presentes em: index.py
O serviço de atualização diária dos artigos ocorrerá automaticamente enquanto o arquivo cron.py estiver sendo executado

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This is a challenge by Coodesh