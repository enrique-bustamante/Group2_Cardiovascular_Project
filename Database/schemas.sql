--Creating tables for Cardio_Group2
CREATE TABLE cardio (
	id VARCHAR NOT NULL,
	age INT NOT NULL,
	gender VARCHAR(2) NOT NULL,
	height INT NOT NULL,
	weight DECIMAL NOT NULL,
	ap_hi INT NOT NULL,
	ap_lo INT NOT NULL,
	cholesterol INT NOT NULL,
	gluc INT NOT NULL,
	smoke VARCHAR(2) NOT NULL,
	alco VARCHAR(2) NOT NULL,
	active VARCHAR(2) NOT NULL,
	cardio VARCHAR(2) NOT NULL,
	PRIMARY KEY (id)
);

DROP TABLE cardio;

SELECT * FROM cardio;