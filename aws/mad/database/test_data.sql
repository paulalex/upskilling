

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


