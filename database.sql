BEGIN;
CREATE TABLE allusers (username TEXT, fullname TEXT, email TEXT, password TEXT);
COMMIT;

BEGIN;
INSERT INTO allusers values("pepe35","Pepe Puig","pepe.puig@gmail.com","pepe94");
INSERT INTO allusers values("josete23","Jose Ruiz","jose.te.ruiz@gmail.com","jose1234");
COMMIT;
