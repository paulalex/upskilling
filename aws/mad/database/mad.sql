DROP TABLE IF EXISTS request CASCADE;
DROP TABLE IF EXISTS quote CASCADE;
DROP TABLE IF EXISTS contract_item CASCADE;
DROP TABLE IF EXISTS unit_rates CASCADE;

CREATE TABLE request(
	request_id serial PRIMARY KEY,
	customer_email VARCHAR (50) UNIQUE NOT NULL,
	customer_reference VARCHAR (50) NOT NULL
);

CREATE TABLE quote(
	quote_id serial PRIMARY KEY,
    request_id integer REFERENCES request (request_id) ON DELETE CASCADE,
    company_reg_number VARCHAR (20),
    registered_postcode VARCHAR (20)
);

CREATE TABLE contract_item(
	c_id serial PRIMARY KEY,
    quote_id integer REFERENCES quote (quote_id) ON DELETE CASCADE,
	mpan VARCHAR (20) UNIQUE NOT NULL
);

CREATE TABLE unit_rates(
	u_id serial PRIMARY KEY,
    c_id integer REFERENCES contract_item (c_id) ON DELETE CASCADE,
	rate_description VARCHAR (50),
	rate_value integer
);


INSERT INTO request VALUES(DEFAULT, 'customer1@email.com', '123');
INSERT INTO request VALUES(DEFAULT, 'customer2@email.com', '456');
INSERT INTO request VALUES(DEFAULT, 'customer3@email.com', '789');
INSERT INTO request VALUES(DEFAULT, 'customer4@email.com', '101112');
INSERT INTO request VALUES(DEFAULT, 'customer5@email.com', '131415');
SELECT * from request;

INSERT INTO quote VALUES(DEFAULT, 1, '11111', 'DT4 9HJ');
INSERT INTO quote VALUES(DEFAULT, 2, '22222', 'EX14 3DW');
INSERT INTO quote VALUES(DEFAULT, 3, '33333', 'E10 6JQ');
INSERT INTO quote VALUES(DEFAULT, 4, '44444', 'SP1 3UA');
INSERT INTO quote VALUES(DEFAULT, 5, '55555', 'BS16 1PR');
SELECT * from quote;

INSERT INTO contract_item VALUES(DEFAULT, 1, 'MPAN1');
INSERT INTO contract_item VALUES(DEFAULT, 2, 'MPAN2');
INSERT INTO contract_item VALUES(DEFAULT, 3, 'MPAN3');
INSERT INTO contract_item VALUES(DEFAULT, 4, 'MPAN4');
INSERT INTO contract_item VALUES(DEFAULT, 5, 'MPAN5');
SELECT * from contract_item;

INSERT INTO unit_rates VALUES(DEFAULT, 1, '', 1);
INSERT INTO unit_rates VALUES(DEFAULT, 2, '', 2);
INSERT INTO unit_rates VALUES(DEFAULT, 3, '', 3);
INSERT INTO unit_rates VALUES(DEFAULT, 4, '', 4);
INSERT INTO unit_rates VALUES(DEFAULT, 5, '', 5);
SELECT * from unit_rates;


