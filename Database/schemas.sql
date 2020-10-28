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

SELECT med.id,
	med.age,
	med.gender,
	med.height,
	med.weight,
	med.ap_hi,
	med.ap_lo,
	med.cholesterol,
	med.glc,
	med.bmi,
	be.smoke,
	be.alco,
	be.active,
	be.cardio
INTO cardio_combined
FROM medical as med
LEFT JOIN behavior as be
ON med.id = be.id;
