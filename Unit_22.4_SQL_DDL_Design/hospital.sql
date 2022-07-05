DROP DATABASE IF EXISTS hospital;

CREATE DATABASE hospital;

\c hospital

CREATE TABLE doctors (
  id SERIAL PRIMARY KEY,
  name text NOT NULL,
  specialty text NOT NULL
);

CREATE TABLE patients (
  id SERIAL PRIMARY KEY,
  name text NOT NULL
);

CREATE TABLE medical_conditions (
  id SERIAL PRIMARY KEY,
  name text NOT NULL,
  treatment text NOT NULL
);

CREATE TABLE patient_doctor_pairs (
  id SERIAL PRIMARY KEY,
  patient_id int REFERENCES patients(id),
  doctor_id int REFERENCES doctors(id)
);

CREATE TABLE patient_medical_history (
  id SERIAL PRIMARY KEY,
  patient_id int REFERENCES patients(id),
  med_cond_id int REFERENCES medical_conditions(id)
);

CREATE TABLE appointments (
  id SERIAL PRIMARY KEY,
  pt_doc_pair_id int REFERENCES patient_doctor_pairs(id),
  chief_complaint text DEFAULT 'wellness check',
  time timestamp NOT NULL
);

CREATE TABLE appointment_new_diagnoses (
  id SERIAL PRIMARY KEY,
  appt_id int REFERENCES appointments(id),
  med_cond_id int REFERENCES medical_conditions(id)
);

INSERT INTO patients(name)
VALUES 
('John Doe'),
('Jane Smith'),
('Jerry Brown');

INSERT INTO doctors(name, specialty)
VALUES 
('Heart Doc A', 'cardiology'),
('Heart Doc B', 'cardiology'),
('Lung Doc', 'pulmonology'),
('Joint Doc', 'orthopedics');

INSERT INTO medical_conditions(name, treatment)
VALUES 
('Hypertension', 'Beta-blockers'),
('Asthma', 'Inhaled steroids'),
('Ganglion cyst', 'Drainage and removal');

INSERT INTO patient_doctor_pairs(patient_id, doctor_id)
VALUES 
(1, 1),
(1, 3),
(1, 4),
(2, 1),
(3, 2),
(3, 3);

INSERT INTO appointments(pt_doc_pair_id, chief_complaint, time)
VALUES 
(1, 'Headaches, fatigue', '2022-08-01 10:30:00'),
(1, 'Wheezing, fatigue', '2022-08-02 11:45:00');

INSERT INTO appointment_new_diagnoses(appt_id, med_cond_id)
VALUES
(1, 1),
(2, 2),
(2, 1);

SELECT p.name, d.name, d.specialty, a.chief_complaint, a.time AS appt_time, m.name AS diagnosis, m.treatment 
FROM patients p 
JOIN patient_doctor_pairs pdp 
ON p.id = pdp.patient_id 
JOIN doctors d 
ON pdp.doctor_id = d.id 
LEFT JOIN appointments a 
ON pdp.id = a.pt_doc_pair_id 
LEFT JOIN appointment_new_diagnoses a_n_d 
ON a.id = a_n_d.appt_id 
LEFT JOIN medical_conditions m 
ON a_n_d.med_cond_id = m.id;