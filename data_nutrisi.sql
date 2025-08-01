CREATE DATABASE IF NOT EXISTS data_nutrisi;
USE data_nutrisi;   

CREATE TABLE IF NOT EXISTS makanan (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nama_makanan VARCHAR(100) NOT NULL,
    kalori FLOAT,
    protein FLOAT,
    lemak FLOAT,
    karbohidrat FLOAT,
    serat FLOAT,
    air FLOAT,
    kalsium FLOAT,
    zatbesi FLOAT
);
INSERT INTO makanan (nama_makanan, kalori, protein, lemak, karbohidrat, serat, air, kalsium, zatbesi) VALUES
('Nasi', 180, 3.0, 0.3, 39.8, 0.2, 56.7, 25, 0.4),
('Nasi tim', 120, 2.4, 0.4, 26.0, 0.5, 71.0, 3, 0.7),
('Nasi merah', 149, 2.8, 0.4, 32.5, 0.3, 64.0, 6, 0.8),
('Bihun goreng', 381, 6.1, 3.9, 80.3, NULL, 9.0, 266, 2.9),
('Jagung rebus', 142, 5.0, 0.7,30.2, 0.8, 53.2, 105, 0.8),
('Ketupat', 212, 4.0, 4.6, 38.6, 0.2, 52.0, 6, 0.7),
('Ketan hitam', 182, 4.0, 1.2, 37.3, 0.3, 56.9, 9, 0.7),
('Tapai Ketan hitam', 172, 3.0, 0.5, 37.5, 0.6, 58.9, 9, 0.7),
('Ketan putih', 163, 3.0, 0.4, 35.7, 0.2, 60.7, 9, 0.7),
('Misoa', 345, 8.5, 2.2, 78.0, 0.5, 10.0, 44.0, 8.7),
('Bakwan', 280, 8.2, 10.2, 39.0, 3.4, 40.5, 204, 7.0),
('Bakpia', 272, 8.7, 6.7, 44.1, 0.9, 38.9, 194, 4.5),
('Bika Ambon', 199, 2.1, 1.5, 44.4, 0.3, 51.5, 45, 1.8),
('Gemblong', 274, 1.7, 5.4, 55.5, 2.2, 36.2, 69, 3.3),
('Ketoprak', 153, 7.9, 7.7, 13.0, 2.9, 69.1, 153, 3.4),
('Kelepon', 215, 3.7, 3.7, 41.8, 1.0, 49.6, 232, 3.3),
('Kue Sus', 221, 7.5, 10.2, 24.8, NULL, 56.6, 105, 2.5),
('Putu Mayang', 121, 1.7, 3.4, 21.1, NULL,73.2, NULL, NULL),
('Mie Aceh', 113, 3.0, 3.2, 18.1, NULL, 74.6, 22, 1.4),
('Mie Bakso', 114, 5.3, 3.0, 16.4, 0.1, 74.5, 286, 1.9);

