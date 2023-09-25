-- Знайти студента із найвищим середнім балом з певного предмета
SELECT s.fullname, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN disciplines d ON d.id = g.disciplines_id 
WHERE d.id = 1
GROUP BY s.fullname
ORDER BY average_grade DESC
LIMIT 1;