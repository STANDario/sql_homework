-- Список курсів, які певному студенту читає певний викладач
SELECT s.fullname, d.name, t.fullname
FROM grades g 
JOIN students s ON s.id = g.student_id 
JOIN disciplines d ON d.id = g.disciplines_id 
JOIN teachers t ON t.id = d.teacher_id 
WHERE s.id = 3 AND t.id = 3
GROUP BY d.name