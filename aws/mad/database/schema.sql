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