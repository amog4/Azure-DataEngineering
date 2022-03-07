-- create a new table in azure sql 

create table facttrips (

    tripid int,
    customerid int,
    lastmodifedtime datetime

);

insert into dbo.facttrips values (100,200,current_timestamp);
insert into dbo.facttrips values (101,201,current_timestamp);
insert into dbo.facttrips values (102,202,current_timestamp);


-- create a watermark table which stores the max datetime

CREATE TABLE watermarktable 
    ( [TableName] VARCHAR(100), [WatermarkValue] DATETIME, );


-- create a stored procedure when every there is an update

create procedure dbo.updatewatermark
@lastmodifedtime DATETIME, 
@TableName VARCHAR(100)

as
begin
update  watermarktable
set WatermarkValue = @lastmodifedtime
where TableName = @TableName
end

