-- Знайти оцінки студентів у окремій групі з певного предмета
SELECT gr.name, d.name,s.fullname, g.grade
FROM grades g 
JOIN students s ON s.id = g.student_id 
JOIN groups gr ON gr.id = s.group_id 
JOIN disciplines d ON d.id = g.disciplines_id
WHERE gr.id = 1 AND d.id = 1
ORDER BY g.grade DESC