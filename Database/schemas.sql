-- Creating table for Cardio Group 2
CREATE TABLE medical (
	id VARCHAR NOT NULL,
	age INT NOT NULL,
	gender INT NOT NULL,
	height INT NOT NULL,
	weight INT NOT NULL,
	ap_hi INT NOT NULL,
	ap_lo INT NOT NULL,
	cholesterol INT NOT NULL,
	glc INT NOT NULL,
	bmi FLOAT NOT NULL
);

CREATE TABLE behavior (
	id VARCHAR NOT NULL,
	smoke VARCHAR NOT NULL,
	alco VARCHAR NOT NULL,
	active VARCHAR NOT NULL,
	cardio VARCHAR NOT NULL
);

DROP TABLE medical;

DROP TABLE behavior;



SELECT * FROM medical;

SELECT * FROM behavior;

--Joining medical and behavior tables

SELECT medical.id,
	medical.age,
	medical.gender,
	medical.height,
	medical.weight,
	medical.ap_hi,
	medical.ap_lo,
	medical.cholesterol,
	medical.glc,
	medical.bmi
FROM medical
LEFT JOIN behavior
ON medical.id = behavior.id;
