library("RMySQL");
# Create a connection Object to MySQL database.
# We will connect to the sampel database named "testdb" that comes with MySql installation.
mysqlconnection = dbConnect(MySQL(), user = 'root', password = '', dbname = 'testcsv', host = 'localhost')
# List the tables available in this database.
print(dbListTables(mysqlconnection))
result = dbSendQuery(mysqlconnection, "select * from grados where universidad = 'Universidad de Córdoba' and RAMA <> 'TOTAL'")
# Fetch the result into a data frame.
df = fetch(result, n = -1)
print(df)
freq<-table(df$rama, dnn = "rama")
print(freq)
# Close the connection. 
dbDisconnect(mysqlconnection)
plazas<-subset(df, medida=="Nº de plazas ofertadas")
print(plazas)
barplot (plazas$valor, main = "anual", ylab = "Plazas Of.", col = "blue", names.arg = plazas$rama, las = 2) # nolint
 