SELECT      
JSON_VALUE(doc, '$.firstname') AS firstname, 
JSON_VALUE(doc, '$.lastname') AS lastname,
 CAST(JSON_VALUE(doc, '$.id') AS INT) as driverid, 
 CAST(JSON_VALUE(doc, '$.salary') AS INT) as salary
  FROM openrowset( BULK 'abfss://path/to/json/*.json',
  format = 'csv',
  fieldterminator = '0x0b',
  fieldquote = '0x0b')

WITH (doc nvarchar(max)) AS ROWS
 GO
