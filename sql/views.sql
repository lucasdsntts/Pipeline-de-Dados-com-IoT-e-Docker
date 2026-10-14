-- 1. Média de temperatura por dispositivo/sala
CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
SELECT "room_id/id" AS device_id, AVG(temp) AS avg_temp
FROM temperature_readings
GROUP BY "room_id/id";

-- 2. Contagem de leituras por hora do dia
CREATE OR REPLACE VIEW leituras_por_hora AS
SELECT 
    EXTRACT(HOUR FROM TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI')) AS hora, 
    COUNT(*) AS contagem
FROM temperature_readings
GROUP BY hora
ORDER BY hora;

-- 3. Temperaturas máximas e mínimas por dia
CREATE OR REPLACE VIEW temp_max_min_por_dia AS
SELECT 
    TO_DATE(SUBSTRING(noted_date FROM 1 FOR 10), 'DD-MM-YYYY') AS data, 
    MAX(temp) AS temp_max, 
    MIN(temp) AS temp_min
FROM temperature_readings
GROUP BY data
ORDER BY data;