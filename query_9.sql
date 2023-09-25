-- Знайти список курсів, які відвідує студент
SELECT s.fullname, d.name
FROM grades g 
JOIN students s ON s.id = g.student_id 
JOIN disciplines d ON d.id = g.disciplines_id 
WHERE s.id = 12
GROUP BY d.name 