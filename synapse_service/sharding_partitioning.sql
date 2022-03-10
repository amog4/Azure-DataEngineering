-- hash
create table dbo.TripTable 
(

    tripId int not null,
    driverId int not null,
    customerId int not null,
    tripDate int,
    startLocation VARCHAR(40),
    endLocation VARCHAR(40)



)

with (clustered columnstore index,
        distribution = hash(tripid),
        PARTITION (tripDate RANGE RIGHT FOR VALUES ( 20220101, 20220201, 20220301 ) 

)
))


INSERT INTO dbo.TripTable VALUES (100, 200, 300, 20220101, 'New York', 'New Jersey');
 
-- replicate 
create table dbo.TripTable 
(

    tripId int not null,
    driverId int not null,
    customerId int not null,
    tripDate int,
    startLocation VARCHAR(40),
    endLocation VARCHAR(40)



)

with (clustered columnstore index,
        distribution =  replicate,
        PARTITION (tripDate RANGE RIGHT FOR VALUES ( 20220101, 20220201, 20220301 ) 

)
))