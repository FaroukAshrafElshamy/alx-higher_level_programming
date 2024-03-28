-- A script that create second table in DB hbtn_0c_0
Create table if not exists second_table(
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score) VALUES 
(1, "John", 10),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8);